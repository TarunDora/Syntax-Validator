import ply.lex as lex
# Change the token names to uppercase
tokens = (
    'STRUCT',
    'TYPEDEF',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'INT',
    'IDENTIFIER',
    'FLOAT',
    'CHAR',
    'DOUBLE',
    'SEMI_COLON',
    'SQ_OPEN_BRACE',
    'SQ_CLOSE_BRACE',
    'ASTERISK',
    'NUMBER'
)
# Regular expression rules for tokens
def t_STRUCT(t):
    r'struct'
    return t
def t_TYPEDEF(t):
    r'typedef'
    return t
def t_INT(t):
    r'int'
    return t
def t_FLOAT(t):
    r'float'
    return t
def t_CHAR(t):
    r'char'
    return t
def t_DOUBLE(t):
    r'double'
    return t

t_SQ_OPEN_BRACE = r'\['
t_SQ_CLOSE_BRACE = r'\]'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z_]\w*'
t_ignore = ' \t'
t_SEMI_COLON=r'\;'
t_ASTERISK=r'\*'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
