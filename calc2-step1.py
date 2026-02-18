import ply.lex as lex

# 1. Define the List of Tokens

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    
)

# 2. Define Token Patterns
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return(t)

def t_PLUS(t):
    r'\+'
    return(t)

def t_MINUS(t):
    r'\-'
    return(t)



def t_error(t):
    # This skips characters that don't match words or numbers (like punctuation)
    t.lexer.skip(1)
    

lexer = lex.lex()
#text_input = "- 9 8 * 4"
          
#lexer.input(text_input)
#
#print ("evaluating: ",text_input)
# while (True):
#    tok = lexer.token()
#    
#    if not tok:
#        break  # No more input
#        
#    print (tok.type)
#
import ply.yacc as yacc

# Import the tokens from your lexer
# (Assuming the lexer code is above this in the same file)

# 1. Define Precedence (Lowest to Highest)

# 2. Define the Grammar Rules
# 1. Define Precedence (Lowest to Highest)


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]
    
    
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
                  
    
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    

    
# 3. Build the Parser
parser = yacc.yacc()

# 4. Test it out
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(f"Result: {result}")