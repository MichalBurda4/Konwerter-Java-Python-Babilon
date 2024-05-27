from antlr4 import *
from java_babilon_lexer import java_babilon_lexer
from java_babilon_parser import java_babilon_parser
from java_babilon_parserListener import java_babilon_parserListener





def parse_java_code(java_code):
    input_stream = InputStream(java_code)
    lexer = java_babilon_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_babilon_parser(token_stream)
    tree = parser.program()

    listener = java_babilon_parserListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.python_code


with open('java_code.txt') as f:
    java_code = f.read()

python_code = parse_java_code(java_code)
print(python_code)
