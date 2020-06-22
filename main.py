import px_lexer
import px_parser
import px_interpreter

from sys import *

#DENGAN MASUKAN .px
lexer = px_lexer.BasicLexer()
parser = px_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    px_interpreter.BasicExecute(tree, env)
