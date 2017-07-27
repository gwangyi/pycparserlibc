from ply import cpp, lex

from . import fake
import os


class Preprocessor(cpp.Preprocessor):
    def __init__(self, lexer=None):
        if lexer is None:
            lexer = lex.lex(module=cpp)
        super().__init__(lexer)
        self._prev_source = None


    def parsegen(self, input, source=None):
        for tok in super().parsegen(input, source):
            if self._prev_source != self.source:
                self._prev_source = self.source
                if self.source:
                    line_dir = f'# {tok.lineno} "{self.source}"\n'
                else:
                    line_dir = f'# {tok.lineno}\n'
                for t in self.tokenize(line_dir):
                    yield t
            yield tok

    # ----------------------------------------------------------------------
    # include()
    #
    # Implementation of file-inclusion
    # ----------------------------------------------------------------------

    def include(self,tokens):
        # Try to extract the filename and then process an include file
        if not tokens:
            return
        if tokens:
            if tokens[0].value != '<' and tokens[0].type != self.t_STRING:
                tokens = self.expand_macros(tokens)

            if tokens[0].value == '<':
                # Include <...>
                i = 1
                while i < len(tokens):
                    if tokens[i].value == '>':
                        break
                    i += 1
                else:
                    print("Malformed #include <...>")
                    return
                filename = "".join([x.value for x in tokens[1:i]])
                if filename.split('/', 1)[0] in fake.libc_headers:
                    return
                path = self.path + [""] + self.temp_path
            elif tokens[0].type == self.t_STRING:
                filename = tokens[0].value[1:-1]
                path = self.temp_path + [""] + self.path
            else:
                print("Malformed #include statement")
                return
        for p in path:
            iname = os.path.join(p,filename)
            try:
                data = open(iname,"r").read().rstrip("\n") + "\n\n"
                dname = os.path.dirname(iname)
                if dname:
                    self.temp_path.insert(0,dname)
                for tok in self.parsegen(data,iname):
                    yield tok

                if dname:
                    del self.temp_path[0]
                break
            except IOError:
                pass
        else:
            print("Couldn't find '%s'" % filename)
