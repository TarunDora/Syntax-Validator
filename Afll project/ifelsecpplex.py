import ply.lex as lex
# Change the token names to uppercase
tokens = (
    'IF',
    'ELSE',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'EQUAL',
    'NUMBER',
    'LESS_THAN',
    'GREATER_THAN',
    'IDENTIFIER',
    'NOT_EQUAL',
    'COUT',
    'RETURN',
    'QUOTE',
    'SEMI_COLON',
    'STD',
    'ENDL'
)

# Regular expression rules for tokens
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_COUT(t):
    r'cout'
    return t
def t_ENDL(t):
    r'endl'
    return t
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_LESS_THAN = r'\<'
t_GREATER_THAN = r'\>'
t_EQUAL = r'\=\='
t_NOT_EQUAL=r'\!\='
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z_]\w*'
# Ignore spaces and tab
t_ignore = ' \t'
t_QUOTE=r'\"'
t_SEMI_COLON=r'\;'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.input('x = 3 * 4 + 5 * 6')
while True:
     tok = lexer.token()
     if not tok: 
          break
     print(tok)