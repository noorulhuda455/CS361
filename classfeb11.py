import ply.lex as lex

# -------------------
# TOKENS
# -------------------

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
)

t_PLUS  = r'\+'
t_MINUS = r'-'

def t_NUMBER(t):
    r'[0-9]+'
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
print("evaluating: ", formatted)

# Send input to lexer
lexer.input(text_input)

# Print token types
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type)
