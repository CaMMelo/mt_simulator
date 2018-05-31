import enum
from lexer import tokenize, TokenType

@enum.unique
class Symbol(enum.Enum):

    PROGRAMA    = enum.auto()
    BLOCO       = enum.auto()
    TRANSICOES  = enum.auto()
    TRANSICAO   = enum.auto()
    PARADA      = enum.auto()
    MOVIMENTO   = enum.auto()

def parse(filename):

    buffer = tokenize(filename)
    pilha = [Symbol.PROGRAMA]

    for token in buffer:

        symbol = pilha[0]
        del pilha[0]

        pilha = table[symbol][token[0]] + pilha

parse('test')
