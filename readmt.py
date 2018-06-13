import machine

def readFile(filedir):
    '''Le o arquivo e retorna as linhas'''
    def read():
        try:
            fn=open(filedir,"U")
        except IOError:
            print("Error: File does not appear to exist.")
            return 0

        with fn as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        return content

    '''Se existir comentario os remove'''
    def removeComent(linha):
        if ";" in linha:
            index = linha.index(";")
            if index == 0:
                return ""
            else:
                vet = linha.split(";")
                return vet[0]
        else:
            return linha

    '''Identifica a linha'''
    def identify():
        content = read()
        bloco   = False
        mt = {}
        geral = []
        for c in content:
            c = removeComent(c)
            vet = c.split()
            if len(vet) > 0:
                if bloco == False and vet[0] == "bloco":
                    bloco = True
                    mt[vet[1]] = (vet[2],"")
                    vetTrans = {}
                    t = {}
                    s = {}

                elif vet[0] == "fim":
                    geral.append(vetTrans)
                    bloco = False

                elif bloco == True:
                    # Identifica CALL com breakpoint espaçado
                    if len(vet) == 4 and vet[3] == "!":
                        #t[vet[0]] = (0,vet[q],True)
                        #vetTrans.append(t[vet[0]])
                        vetTrans[vet[0]] = (0,vet[1],True)
                    # Identifica CALL com breakpoint ou não
                    elif len(vet) == 3:
                        if "!" in vet[2]:
                            vet[2] = vet[2].replace("!","")
                            #t[vet[0]] = (0,vet[1],True)
                            #vetTrans.append(t[vet[0]])
                            vetTrans[vet[0]] = (0,vet[1],True)
                        else:
                            #t[vet[0]] = (0,vet[1],False)
                            #vetTrans.append(t[vet[0]])
                            vetTrans[vet[0]] = (0,vet[1],False)


                    # Identifica Instrução
                    elif len(vet) == 6 or len(vet) == 7:
                        source = vet[0]
                        _read = vet[1]
                        write = vet[3]
                        target = vet[5]
                        bp = False

                        if source not in vetTrans:
                            vetTrans[source] = (1, {})

                        #Define a posição
                        if vet[4] == "i":
                            pos = 0
                        elif vet[4] == "e":
                            pos = -1
                        elif vet[4] == "d":
                            pos = 1
                        # Identifica Ins com Breakpoint Espaçado
                        if len(vet) == 7 and vet[6] == "!":
                            bp = True
                        # Identifica Ins com Breakpoint
                        elif "!" in vet[5]:
                            bp = True
                            target = target.replace("!","")
                        # Identifica instrução
                        else:
                            bp = False

                        trans = (write, pos, target, bp)
                        vetTrans[source][1][_read] = trans


        return geral
    mt = identify()
    for m in mt:
        print("=================")
        print(m)
        print("=================")

if __name__ == "__main__":
    readFile("turing.mt")
