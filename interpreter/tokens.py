class RawToken:
    def __init__(self, details=None):
        self.details = details
    
    def __repr__(self):
        if self.details == None:
            return f"{self.__class__.__name__}"
        return f"{self.__class__.__name__}<\033[92m{self.detail_repr()}\033[0m>"

class Name(RawToken):
    def detail_repr(self):
        return self.details

class Literal(RawToken):
    ...

class LiteralStr(Literal):
    def detail_repr(self):
        return f'{self.details}'

class LiteralNum(Literal):
    def detail_repr(self):
        return self.details

class Operator(RawToken):
    def detail_repr(self):
        return self.details

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