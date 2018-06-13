# the state machine:
# {
#     state: (TAPE, {
#         read: (write, go, target, BREAKPOINT)
#     }),
#      #writ
#     state: (CALL, target, BREAKPOINT)
# }

# the machine:
# {
#     procedure_name: (initial, state_machine)
# }

CALL = 0
TAPE = 1

DIREITA     = 1
IMOVEL      = 0
ESQUERDA    = -1

RETORNE = -1
PARE    = -2

class VirtualMachine:

    procedures = {
        'main': None
    }

    __tape = []
    tape_pos = 0

    def __init__(self, procedures, head='()'):

        self.procedures = {
            **self.procedures,
            **procedures
        }

        self.head = head

    def start(self, word):
        ''' Prepara a máquina para ser executada sobre uma palabra '''

        self.__tape = [x for x in word]
        self.tape_pos = 0
        self.stack = [['main', self.procedures['main'][0]], ]

    def show_current_state(self):
        ''' Exibe o estado presente do cabeçote da máquina '''

        p, s = self.stack[-1]

        left = ''.join(self.__tape[max(0, self.tape_pos-20 ), self.tape_pos])
        right = ''.join(self.__tape[self.tape_pos+1:min(len(self.__tape), self.tape_pos + 1 + 20)])
        print(f'{p:.>16}.{s:04}:{left:_>20}{head[0]}{self.__tape[self.tape_pos]}{self.head[1]}{right:_<20}')

    @property
    def tape(self):
        ''' representação da fita em string '''
        return ''.join(self.__tape)

    def run(self, verbose=False, steps=500):
        ''' Executa n computações dessa máquina, retorna True caso a execução
            tenha terminado '''

        while len(self.stack) > 0:

            if steps == 0:
                return False

            steps -= 1

            p, s = self.stack[-1]
            action, symbols = self.procedures[p][s]


            if verbose:
                self.show_current_state()

            if action == CALL: # faz uma chamada de procedimento

                self.stack.append((a[1], self.procedures[a[1]][0]))
                continue

            write, go, target = symbols[self.__tape[self.tape_pos]]

            self.__tape[self.tape_pos] = write
            self.tape_pos += go

            if self.tape_pos < 0:
                self.__tape = [None,] + self.__tape
                self.tape_pos = 0
            elif self.tape_pos == len(self.__tape):
                self.__tape += [None,]

            if target == PARE: # para a execução da máquina
                return True

            if target == RETORNE: # remove um item do topo da pilha

                del self.stack[-1]

                if len(self.stack) > 0:
                    p, s = self.stack[-1]
                    _, target = self.procedures[p][s]
                else:
                    break

            self.procedures[1] = target

        return True
