import ply.lex as lex
from rules import *


def lexer_action(data):
    token_list = []
    lexer = lex.lex()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type, tok.value, tok.lineno))
    return token_list
