import ply.lex as lex
import sys
# que tome encuena los operadoes
tokens = ('NUMBER', 't_OPERADORES', 'ID', 'FLOAT')

t_OPERADORES = r'[-+*/]'
t_NUMBER = r'\d+'
t_ID = r'[a-zA-Z_]\w*'
t_ignore = ' \t\n'

def t_FLOAT(t):
    r'\d+\.\d+'
    return t

def t_error(t):
    print("Caracter ilegal:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    input_text = input("Ingresa texto: ")
    lexer.input(input_text)
    for tok in lexer:
        print(tok)
