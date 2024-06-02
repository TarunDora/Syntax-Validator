import ply.yacc as yacc
from switch import tokens
import sys

# Define the start symbol
start = 'statement'

# Grammar rules
# Use uppercase tokens in the parser
def p_statement(p):
    '''
    statement : SWITCH OPEN_PAREN switch_expression CLOSE_PAREN OPEN_BRACE switch_body CLOSE_BRACE
                | SWITCH OPEN_PAREN switch_expression CLOSE_PAREN OPEN_BRACE switch_body DEFAULT COLON statements CLOSE_BRACE
                | SWITCH OPEN_PAREN switch_expression CLOSE_PAREN OPEN_BRACE switch_body DEFAULT COLON statements BREAK SEMI_COLON CLOSE_BRACE
        '''
    pass

def p_switch_expression(p):
    '''
    switch_expression : empty
                        | NUMBER
                        | IDENTIFIER
                '''
    pass

def p_expression(p):
    '''
    expression : IDENTIFIER
                | NUMBER
    '''
    pass

def p_statements(p):
    '''
    statements : empty
                | IDENTIFIER SEMI_COLON statements
                | NUMBER SEMI_COLON statements
                | RETURN IDENTIFIER SEMI_COLON statements
                | COUT LESS_THAN LESS_THAN NUMBER SEMI_COLON statements
                | COUT LESS_THAN LESS_THAN QUOTE IDENTIFIER QUOTE SEMI_COLON statements
                | COUT LESS_THAN LESS_THAN QUOTE NUMBER QUOTE SEMI_COLON statements
    '''
    pass

def p_switch_body(p):
    '''
    switch_body : CASE expression COLON statements BREAK SEMI_COLON switch_body
            | CASE expression COLON switch_body
            | CASE expression COLON statements switch_body
            | empty
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
    print("invalid switch statement")
    sys.exit(1)

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            data = input("Enter an switch statement:")
            if not data:
                break
            parser.parse(data)
            print("Valid switch statement")
        except EOFError:
                break
