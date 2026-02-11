import ply.lex as lex
# List of token names
tokens = (
    'NUMBER',
    'WORD',
)

# Regular expression rules for simple tokens
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    #print(t)
    return t

def t_WORD(t):
    r'[a-zA-Z]+'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\n'
# Error handling rule

def t_error(t):
    t.lexer.skip(1)

    # This skips characters that don't match words or
    #numbers (like punctuation)

lexer = lex.lex()
text_input = "In 2026, I have 5 apples,2 kiwi and some bread."
lexer.input(text_input)
while (True):
    tok = lexer.token()
    #print(tok)
    if not tok:
        break # No more input
    if tok.type == 'WORD':
        print ("Word ",tok.value)
    elif tok.type == 'NUMBER':
        print ("Number: ",tok.value)



