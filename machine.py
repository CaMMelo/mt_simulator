# {
#     id: state_machine
# }

class Machine:

    tape = []

    procedures = {
        'main': None
    }

    def __init__(self, procedures):

        self.procedures = {
            **self.procedures,
            **procedures
        }

    def __str__(self):
        str_ = ''
        return str_

    def run(self, word):

        self.tape = [x for x in word]
