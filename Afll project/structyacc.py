import ply.yacc as yacc
from structlex import tokens
import sys

# Define the start symbol
start = 'statement'

# Grammar rules
# Use uppercase tokens in the parser
def p_statement(p):
    '''
    statement : STRUCT IDENTIFIER OPEN_BRACE struct_body CLOSE_BRACE SEMI_COLON
                | TYPEDEF STRUCT IDENTIFIER OPEN_BRACE struct_body CLOSE_BRACE IDENTIFIER SEMI_COLON
    '''
    pass

def p_struct_body(p):
    '''
    struct_body : INT IDENTIFIER SEMI_COLON struct_body
                | empty
                | FLOAT IDENTIFIER SEMI_COLON struct_body
                | DOUBLE IDENTIFIER SEMI_COLON struct_body
                | CHAR IDENTIFIER SQ_OPEN_BRACE NUMBER SQ_CLOSE_BRACE SEMI_COLON struct_body
                | STRUCT IDENTIFIER ASTERISK IDENTIFIER SEMI_COLON struct_body
                '''
    pass


def p_empty(p):
    "empty :"
    pass
# Error handling
def p_error(p):
    #global a
    #a=1
    if p:
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")
    print("invalid struct statement")
    sys.exit(1)

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            data = input("Enter an struct statement:")
            if not data:
                break
            parser.parse(data)
            print("Valid struct statement")
        except EOFError:
                break
