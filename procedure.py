# {
#     state: (A, read, write, go, target)
#     state: (B, procedure, target)
# }

class Procedure:

    def __init__(self, initial, states):

        self.initial = initial
        self.states  = states
