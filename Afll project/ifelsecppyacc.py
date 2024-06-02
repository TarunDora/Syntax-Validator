import ply.yacc as yacc
from ifelsecpplex import tokens
import sys

# Define the start symbol
start = 'statement' 

# Grammar rules
# Use uppercase tokens in the parser
def p_statement(p):
    '''
    statement : IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE 
                | IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE statement
              | IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE ELSE IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE statement
              | IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE ELSE IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE ELSE OPEN_BRACE if_body CLOSE_BRACE
              | IF OPEN_PAREN if_expression CLOSE_PAREN OPEN_BRACE if_body CLOSE_BRACE ELSE OPEN_BRACE if_body CLOSE_BRACE statement
              | empty
    '''
    pass

def p_if_body(p):
    '''
    if_body : empty
                | COUT LESS_THAN LESS_THAN QUOTE IDENTIFIER QUOTE SEMI_COLON
                | COUT LESS_THAN LESS_THAN QUOTE NUMBER QUOTE SEMI_COLON
                | COUT LESS_THAN LESS_THAN IDENTIFIER SEMI_COLON
                | COUT LESS_THAN LESS_THAN NUMBER SEMI_COLON
                | COUT LESS_THAN LESS_THAN ENDL SEMI_COLON 
                | RETURN IDENTIFIER SEMI_COLON
                '''
    pass

def p_if_expression(p):
    '''if_expression : IDENTIFIER LESS_THAN NUMBER
                     | IDENTIFIER GREATER_THAN NUMBER
                     | IDENTIFIER EQUAL NUMBER
                     | IDENTIFIER LESS_THAN EQUAL NUMBER
                     | IDENTIFIER GREATER_THAN EQUAL NUMBER
                     | IDENTIFIER NOT_EQUAL NUMBER
                     | empty
                     | IDENTIFIER
                     | NUMBER
                     | NUMBER LESS_THAN NUMBER
                     | NUMBER GREATER_THAN NUMBER
                     | NUMBER EQUAL NUMBER
                     | NUMBER NOT_EQUAL NUMBER
                     | NUMBER LESS_THAN EQUAL NUMBER
                     | NUMBER GREATER_THAN EQUAL NUMBER
                     | IDENTIFIER LESS_THAN IDENTIFIER
                     | IDENTIFIER GREATER_THAN IDENTIFIER
                     | IDENTIFIER EQUAL IDENTIFIER
                     | IDENTIFIER NOT_EQUAL IDENTIFIER
                     | IDENTIFIER LESS_THAN EQUAL IDENTIFIER
                     | IDENTIFIER GREATER_THAN EQUAL IDENTIFIER
                     | NUMBER LESS_THAN IDENTIFIER
                     | NUMBER GREATER_THAN IDENTIFIER
                     | NUMBER EQUAL IDENTIFIER
                     | NUMBER NOT_EQUAL IDENTIFIER
                     | NUMBER LESS_THAN EQUAL IDENTIFIER
                     | NUMBER GREATER_THAN EQUAL IDENTIFIER'''
    
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
    print("invalid if-else statement")
    sys.exit(1)

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            data = input("Enter an if-else statement:")
            if not data:
                break
            parser.parse(data)
            print("Valid if-else statement")
        except EOFError:
            break