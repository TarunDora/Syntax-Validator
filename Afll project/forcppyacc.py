import ply.yacc as yacc
from forcpplex import tokens
import sys

# Define the tokens from the lexer
#tokens = tokens
start='statement'
# Define the parser rules
def p_for_loop(p):
    '''
    statement : FOR LPAREN declaration SEMICOLON condition SEMICOLON next RPAREN OBRACE body CBRACE
    '''

def p_declaration(p):
    '''
    declaration : INT ID EQUAL NUMBER
                | empty
                | ID EQUAL NUMBER
                | INT ID EQUAL ID
                | ID EQUAL ID
    '''

def p_condition(p):
    '''
    condition : ID LESSER_THAN NUMBER
                | empty
                | ID LESSER_THAN ID
                | ID LESSER_THAN EQUAL NUMBER
                | ID LESSER_THAN EQUAL ID
                | ID GREATER_THAN NUMBER
                | ID GREATER_THAN ID
                | ID GREATER_THAN EQUAL NUMBER
                | ID GREATER_THAN EQUAL ID
    '''

def p_next(p):
    '''
    next : ID PLUS PLUS
            | empty
            | ID MINUS MINUS
            | ID PLUS EQUAL NUMBER
            | ID MINUS EQUAL NUMBER
            | ID EQUAL ID PLUS NUMBER
            | ID EQUAL ID MINUS NUMBER
            | ID PLUS EQUAL ID
            | ID MINUS EQUAL ID
            | ID EQUAL ID PLUS ID
            | ID EQUAL ID MINUS ID
    '''

def p_body(p):
    '''
    body : empty
                | COUT OUTPUT QUOTE ID QUOTE SEMICOLON body
                | COUT OUTPUT QUOTE NUMBER QUOTE SEMICOLON body
                | COUT OUTPUT ID SEMICOLON body
                | COUT OUTPUT ID OUTPUT ENDL SEMICOLON body
                | COUT OUTPUT QUOTE ID QUOTE OUTPUT ENDL SEMICOLON body
                | COUT OUTPUT NUMBER SEMICOLON body
                | COUT OUTPUT NUMBER OUTPUT ENDL SEMICOLON body
                | COUT OUTPUT ENDL SEMICOLON body
                | RETURN ID SEMICOLON body
                '''
    pass
def p_empty(p):
    "empty :"
    pass
# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")
    print("invalid for loop")
    sys.exit(1)

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            data = input("Enter a for loop:")
            if not data:
                break
            parser.parse(data)
            print("Valid for loop")
        except EOFError:
            break