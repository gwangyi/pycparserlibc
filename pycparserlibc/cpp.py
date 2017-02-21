try:
    from pycparser.ply import cpp, lex
except ImportError:
    from ply import cpp, lex


class Preprocessor(cpp.Preprocessor):
    def __init__(self, lexer=None):
        if lexer is None:
            lexer = lex.lex(module=cpp)
        super().__init__(lexer)
