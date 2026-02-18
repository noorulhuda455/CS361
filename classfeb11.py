import ply.lex as lex
import ply.yacc as yacc

# -------------------
# TOKENS
# -------------------

#1. Define the list of tokens 

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

# -------------------
# INPUT
# -------------------

text_input = "5+4-2"

# Print formatted expression
formatted = text_input.replace("+", " + ").replace("-", " - ")

#commenting the code below 

# print("evaluating: ", formatted)

# # Send input to lexer
# lexer.input(text_input)

# # Print token types
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok.type)


#code from his presentation

#yacc rules
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


#3. Build the parser 

parser = yacc.yacc()

#4. Test it out 

while True: 
    try: 
        s = input('calc > ')
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    print(f"Result: {result}")
