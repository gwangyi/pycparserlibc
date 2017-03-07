from . import cpp
from . import fake
from pycparser.c_parser import CParser
from pycparser import c_ast

def preprocess(text, filename='', cpp_args='', preprocessor=None, fake_defs=False):
    if not isinstance(cpp_args, list):
        cpp_args = [cpp_args]
    if preprocessor is None:
        p = cpp.Preprocessor()
    else:
        p = preprocessor

    if fake_defs:
        for define in fake.defines:
            p.define(define)

    fake_macros = list(p.macros.keys())

    for cpp_arg in cpp_args:
        if cpp_arg[:2] == '-I':
            p.add_path(cpp_arg[2:])
        elif cpp_arg[:2] == '-D':
            p.define(cpp_arg[2:].replace('=', ' ', 1))

    p.parse(text, filename)

    def gen():
        latest = ''
        while True:
            tok = p.token()
            if not tok:
                return
            if latest != p.source:
                yield '# {} "{}"\n'.format(tok.lineno - 1, p.source)
                latest = p.source
            yield tok.value

    processed = ''.join(gen())
    for m in fake_macros:
        del p.macros[m]

    return processed


def parse(text, filename='', parser=None, fake_typedefs=False):
    if parser is None:
        parser = CParser()

    if fake_typedefs:
        text = ''.join((fake.typedefs,
                        '# {} "{}"\n'.format(0, filename),
                        text))

    ast = parser.parse(text, filename)
    for i in range(len(ast.ext)):
        node = ast.ext[i]
        if isinstance(node, c_ast.Typedef) and node.name == '__end_of_fakes__':
            break

    del ast.ext[:i+1]
    return ast

