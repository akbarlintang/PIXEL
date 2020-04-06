from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Pendefinisian token
    IF = r'JIKA'
    PRINT = r'CETAK'
    THEN = r'MAKA'
    ELSE = r'SELAIN ITU'
    FOR = r'UNTUK'
    FUN = r'FUNGSI'
    TO = r'SAMPAI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='