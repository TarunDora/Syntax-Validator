import ply.lex as lex
# Change the token names to uppercase
tokens = (
    'SWITCH',
    'CASE',
    'DEFAULT',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'NUMBER',
    'IDENTIFIER',
    'COUT',
    'RETURN',
    'SEMI_COLON',
    'BREAK',
    'COLON',
    'LESS_THAN',
    'QUOTE'
    )
# Regular expression rules for tokens
def t_SWITCH(t):
    r'switch'
    return t
def t_CASE(t):
    r'case'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_COUT(t):
    r'cout'
    return t
def t_DEFAULT(t):
    r'default'
    return t
def t_BREAK(t):
    r'break'
    return t

t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_NUMBER = r'[0-9]+'
t_IDENTIFIER = r'[a-zA-Z_]\w*'
t_ignore = ' \t'
t_SEMI_COLON=r'\;'
t_COLON=r'\:'
t_LESS_THAN=r'\<'
t_QUOTE=r'\"'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
