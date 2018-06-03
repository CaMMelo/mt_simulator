import enum
from lexer import tokenize

class Token(enum.Enum):
    TK_NONE     =  0
    TK_BLOCO    =  1  # 'bloco'
    TK_DIRECAO  =  2  # 'd'|'i'|'e'
    TK_FIM      =  3  # 'fim'
    TK_PARE     =  4  # 'pare'
    TK_RETORNE  =  5  # 'retorne'
    TK_DDASH    =  6  # '--'
    TK_PARADA   =  7  # '!'
    TK_BRANCO   =  8  # '_'
    TK_CORINGA  =  9  # '*'

    TK_NUMERO   = 10   # [0-9]
    TK_ALPHA    = 11   # [^ \t\n]
    TK_ESTADO   = 12   # [0-9]{2,4}
    TK_PROCID   = 13   # ([0-9][^ \t\n0-9]+ | [^ \t\n0-9]{2,})[^ \t\n]*


def parse(filename):

    tokens = tokenize(filename)
