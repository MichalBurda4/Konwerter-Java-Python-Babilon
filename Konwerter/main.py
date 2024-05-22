from antlr4 import *
from java_babilon_lexer import java_babilon_lexer
from java_babilonParser import java_babilonParser


def parse_java_code(java_code):
    input_stream = InputStream(java_code)
    lexer = java_babilon_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_babilonParser(token_stream)
    tree = parser.compilationUnit()  # "compilationUnit" to główna reguła w gramatyce JavaParser
    return tree


with open('java_code.txt') as f:
    java_code = f.read()

tree = parse_java_code(java_code)
