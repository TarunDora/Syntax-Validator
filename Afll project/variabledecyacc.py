import ply.yacc as yacc
from a1 import tokens
import sys

# Define the start symbol
start = 'statement' 

# Grammar rules
# Use uppercase tokens in the parser
def p_statement(p):
    '''
    statement  : empty
               | INT IDENTIFIER SEMICOLON statement
               | INT IDENTIFIER EQUAL NUMBER SEMICOLON statement
               | INT IDENTIFIER EQUAL MINUS NUMBER SEMICOLON statement
               | data IDENTIFIER SEMICOLON statement
               | data IDENTIFIER EQUAL NUMBER SEMICOLON statement
               | data IDENTIFIER EQUAL MINUS NUMBER SEMICOLON statement
               | data IDENTIFIER EQUAL NUMBER DECIMAL NUMBER SEMICOLON statement
               | data IDENTIFIER EQUAL MINUS NUMBER DECIMAL NUMBER SEMICOLON statement
               | CHAR IDENTIFIER SEMICOLON statement
               | CHAR IDENTIFIER EQUAL CID SEMICOLON statement
               | STRING IDENTIFIER SEMICOLON statement
               | STRING IDENTIFIER EQUAL SID SEMICOLON statement
               | BOOL IDENTIFIER SEMICOLON statement
               | BOOL IDENTIFIER EQUAL TRUE SEMICOLON statement
               | BOOL IDENTIFIER EQUAL FALSE SEMICOLON statement
               | BOOL IDENTIFIER EQUAL NUMBER SEMICOLON statement
               | BOOL IDENTIFIER EQUAL MINUS NUMBER SEMICOLON statement
               | data1 AMPERSAND IDENTIFIER EQUAL IDENTIFIER SEMICOLON statement
               | data1 STAR IDENTIFIER SEMICOLON statement
               | data1 STAR IDENTIFIER EQUAL AMPERSAND IDENTIFIER SEMICOLON statement
    '''
    pass

def p_data(p):
    '''
    data : DOUBLE
         | FLOAT
    '''
def p_data1(p):
    '''
    data1 : INT
          | FLOAT
          | DOUBLE
          | CHAR
          | STRING
    '''
def p_empty(p):
    "empty :"
    pass
# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")
    print("invalid variable declaration statement")
    sys.exit(1)

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            data = input("Enter a variable declaration statement:")
            if not data:
                break
            parser.parse(data)
            print("Valid variable declaration statement")
        except EOFError:
            break