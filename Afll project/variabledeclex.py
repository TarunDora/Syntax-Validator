import ply.lex as lex
# Change the token names to uppercase
tokens = (
    'EQUAL',
    'NUMBER',
    'IDENTIFIER',
    'CID',
    'SID',
    'SEMICOLON',
    'CHAR',
    'AMPERSAND',
    'STAR',
    'STRING',
    'DOUBLE',
    'FLOAT',
    'DECIMAL',
    'BOOL',
    'MINUS',
    'TRUE',
    'FALSE',
    'INT'
)

# Regular expression rules for tokens
def t_INT(t):
     r'int'
     return t
def t_TRUE(t):
     r'true'
     return t
def t_FALSE(t):
     r'false'
     return t
def t_FLOAT(t):
     r'float'
     return t
def t_DOUBLE(t):
     r'double'
     return t
def t_CHAR(t):
     r'char'
     return t
def t_STRING(t):
     r'string'
     return t
def t_BOOL(t):
     r'bool'
     return t
t_EQUAL = r'\='
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_CID=r'\'[^\']\'*'
t_SID=r'\"[^\"]\"*'
t_ignore = ' \t'
t_SEMICOLON=r'\;'
t_MINUS=r'\-'
t_DECIMAL=r'\.'
t_AMPERSAND=r'\&'
t_STAR=r'\*'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.input('x = 3')
while True:
     tok = lexer.token()
     if not tok: 
          break
     print(tok)