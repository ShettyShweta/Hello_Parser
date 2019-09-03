from antlr4 import *
from HelloLexer import HelloLexer
from HelloListener import HelloListener
from HelloParser import HelloParser
import sys

class HelloPrintListener(HelloListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():

    lexer = HelloLexer(StdinStream())
    print "Lexer entered"
    stream = CommonTokenStream(lexer)
    print "Token entered"
    parser = HelloParser(stream)
    print "Parser entered"
    tree = parser.hi()
    print "Tree entered"
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
