class TokenList(list):
    def __str__(self) -> str:
        out: list = []
        for token in self:
            if token.details != None:
                out.append(f"{token.__class__.__name__}<\033[92m{token.details}\033[0m>")
            else:
                out.append(token.__class__.__name__)
        return " ".join(out)

class BaseToken:
    def __init__(self, details=None):
        self.details = details
    
    def __str__(self):
        if self.details != None:
            return f"{self.__class__.__name__}<\033[92m{self.details}\033[0m>"
        return self.__class__.__name__

# First Level Inheritance
class Name(BaseToken):
    ...

class Literal(BaseToken):
    ...

class NewLine(BaseToken):
    ...

class IndentMinus(BaseToken):
    ...

class IndentPlus(BaseToken):
    _match_end = IndentMinus

# Second Level Inheritance
class LiteralStr(Literal):
    ...

class LiteralNum(Literal):
    ...