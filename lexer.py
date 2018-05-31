import enum
import re

@enum.unique
class TokenType(enum.Enum):
    ''' possíveis tokens encontrados no arquivo de entrada '''

    BLOCO   = enum.auto()   # 'bloco'
    FIM     = enum.auto()   # 'fim'
    DDASH   = enum.auto()   # '--'
    ID      = enum.auto()   # [any-character]+

def Token(tipo, valor):
    return(tipo, valor)

fsm = {
    0: {
        'b': (1, TokenType.ID),
        'f': (6, TokenType.ID),
        '-': (9, TokenType.ID),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    1: {
        'l': (2, TokenType.ID),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    2: {
        'o': (3, TokenType.ID),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    3: {
        'c': (4, TokenType.ID),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    4: {
        'o': (5, TokenType.BLOCO),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    5: {
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    6: {
        'i': (7, TokenType.ID),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    7: {
        'm': (8, TokenType.FIM),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    8: {
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    9: {
        '-': (10, TokenType.DDASH),
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    10: {
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    },

    11: {
        '\n': (0, None),
        None: (11, None)
    },

    12: {
        ';': (11, None),
        ' ': (0, None),
        '\t': (0, None),
        '\n': (0, None),
        None: (12, TokenType.ID)
    }
}

def table(state, char):

    if char in fsm[state]:
        return fsm[state][char]
    return fsm[state][None]

def tokenize(filename):
    ''' return a list of tokens from a stream of characters '''

    start       = 0
    lookahead   = 0
    state       = 0
    match       = None

    tokens = []

    with open(filename, 'rb') as ifile:

        data = ifile.read()
        lexeme = ''

        while lookahead < len(data):

            c = chr(data[lookahead])
            _state, _match = table(state, c)

            if match and not _match:

                    tokens.append(Token(match, lexeme))
                    lexeme = ''
                    match = None

            state = _state
            match = _match
            lookahead += 1

            if match:
                lexeme += str(c)

        # if match:
        #     tokens.append(Token(match, lexeme))

    return tokens
