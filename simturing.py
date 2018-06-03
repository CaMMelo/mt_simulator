import getopt
import sys
from parser import parse
from machine import VirtualMachine

def usage():
    print(f'{sys.argv[0]}: usage: {sys.argv[0]} [options] input_file')
    print('  options:')
    print('    -?, --help       :\t exibe essa tela de ajuda.')
    print('    -r, --resume     :\t executa o programa até o fim em modo silencioso e depois imprime o conteúdo final da fita.')
    print('    -b, --break      :\t para a execução da máquina após N computações e mostra o conteúdo da fita')
    print('    -s, --steps=N    :\t mostra N computações passo a passo na tela, depois abre um prompt e aguarda uma nova opção.')
    print('    -h, --head=DELIM :\t define os caracteres delimitadores do cabeçote')
    print('    -w, --word=WORD  :\t define a palavra de entrada do programa.')

if __name__ == '__main__':

    long_opts = [
        'resume', 'verbose', 'help', 'break', 'steps=', 'head=', 'word='
    ]

    options, args = getopt.gnu_getopt(sys.argv, 'rv?bs:h:w:', long_opts)

    steps   = None
    head    = '()'
    verbose = False
    word    = None
    _break  = False

    for opt, value in options:

        if opt in ('-?', '--help'):
            usage()
            sys.exit(0)

        elif opt in ('-r', '--resume'):

            if steps:
                print(f'{sys.argv[0]}: erro: não é possivel resumir a execução.')
                sys.exit(-1)

            steps = 500
            verbose = False

        elif opt in ('-v', '--verbose'):

            verbose = True

        elif opt in ('-b', '--break'):

            _break = True

        elif opt in ('-s', '--steps'):

            if steps:
                print(f'{sys.argv[0]}: erro: não é possivel definir uma quantidade de passos para execução.')
                sys.exit(-1)

            steps = int(value)
            verbose = True

        elif opt in ('-h', '--head'):

            if len(value) != 2:
                print(f'{sys.argv[0]}: erro: são necessários 2 caracteres para o cabeçote. ex:"<>".')
                sys.exit(-1)

            head = value

        elif opt in ('-w', '--word'):

            if word:
                print(f'{sys.argv[0]}: erro: a palavra da fita já foi definida')
                sys.exit(-1)

            word = value

        else:
            usage()
            sys.exit(-1)

    if len(args) != 2:
        usage()
        sys.exit(-1)

    ifile   = args[1]

    if not steps:
        steps = 500

    if verbose:

        print('Simulador de Máquina de Turing ver 1.0')
        print('Desenvolvido como trabalho pratico para a disciplina de Teoria da Computação')
        print('[Augusto Amaral, Caio Melo], IFMG, 2018.\n')

    # parse the input file
    procedures = parse(ifile)
    machine = VirtualMachine(procedures, head)

    if not word:
        word = input('Forneça a palavra inicial: ')

    machine.start(word)

    long_opts = [
        'resume', 'verbose', 'break', 'steps='
    ]

    while not machine.run(verbose, steps):
        ''' executa a máquina '''

        if _break:
            break

        args = input('Forneça opção (-r -v -s -b): ')
        args = options.split()

        options, _ = getopt.gnu_getopt(args, 'rvbs:', long_opts)

        old_steps = steps

        for opt, value in options:

            if opt in ('-r', '--resume'):

                if (steps != old_steps):
                    print(f'{sys.argv[0]}: aviso: não é possivel resumir aqui.')
                    continue

                steps = 500
                verbose = False

            elif opt in ('-v', '--verbose'):

                verbose = True

            elif opt in ('-b', '--break'):

                _break = True

            elif opt in ('-s', '--steps'):

                if (steps != old_steps):
                    print(f'{sys.argv[0]}: erro: não é possivel redefinir o numero de passos.')
                    continue

                steps = int(value)

            else:
                print(f'{sys.argv[0]}: aviso: opção desconhecida: {opt}.')

    final = machine.tape
    print(final)
