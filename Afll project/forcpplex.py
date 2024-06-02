import ply.lex as lex

# Define the tokens
tokens = (
    'FOR',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ID',
    'INT',
    'LESSER_THAN',
    'GREATER_THAN',
    'EQUAL',
    'PLUS',
    'MINUS',
    'NUMBER',
    'CBRACE',
    'OBRACE',
    'OUTPUT',
    'COUT',
    'ENDL',
    'QUOTE',
    'RETURN'
)

def t_FOR(t):
    r'for'
    return t
def t_INT(t):
    r'int'
    return t
def t_COUT(t):
    r'cout'
    return t
def t_ENDL(t):
    r'endl'
    return t
def t_RETURN(t):
    r'return'
    return t
# Define regular expressions for the tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_ID =r'[a-zA-Z_][a-zA-Z_0-9]*'
t_LESSER_THAN=r'\<'
t_GREATER_THAN=r'\>'
t_EQUAL=r'\='
t_PLUS=r'\+'
t_MINUS=r'\-'
t_NUMBER=r'[0-9]+'
t_OBRACE=r'\{'
t_CBRACE=r'\}'
t_OUTPUT=r'\<\<'
t_QUOTE=r'\"'

# Ignore whitespace and tabs
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()