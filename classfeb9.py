import ply.lex as lex

# Token names
tokens = (
    'VOWEL',
    'CONSONANT',
    'PUNCT',
)

# Counters
vowel_count = 0
consonant_count = 0
punct_count = 0


# Vowel rule
def t_VOWEL(t):
    r'[AEIOUaeiou]'
    global vowel_count
    vowel_count += 1
    return t


# Consonant rule
def t_CONSONANT(t):
    r'[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]'
    global consonant_count
    consonant_count += 1
    return t


# Required punctuation only:
# ( ) , ; : . [ ]
def t_PUNCT(t):
    r'[\(\),;:\.\[\]]'
    global punct_count
    punct_count += 1
    return t


# Ignore spaces and tabs and newlines
t_ignore = ' \t\n'


# Error handling rule (ignore everything else)
def t_error(t):
    t.lexer.skip(1)


# Build lexer
lexer = lex.lex()

# Example input
text_input = "Hello (Noor), welcome to CS;627: AI [Spring]."
lexer.input(text_input)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break

# Final counts
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Punctuation:", punct_count)



