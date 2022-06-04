def output_token_list(tokens: list):
    out: list = []
    for token in tokens:
        if token.details != None:
            out.append(f"{token.__class__.__name__}<\033[92m{token.details}\033[0m>")
        else:
            out.append(token.__class__.__name__)
    print(" ".join(out))

class RawToken:
    def __init__(self, details=None):
        self.details = details

class Name(RawToken):
    ...

class Literal(RawToken):
    ...

class LiteralStr(Literal):
    ...

class LiteralNum(Literal):
    ...

class Operator(RawToken):
    ...

class NewLine(RawToken):
    ...

class IndentPlus(RawToken):
    ...

class IndentMinus(RawToken):
    ...

class OParen(RawToken):
    ...

class CParen(RawToken):
    ...

class Unknown(RawToken):
    ...