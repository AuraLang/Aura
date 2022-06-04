import interpreter.tokens as Tokens

class AST:
    def __init__(self, tokens: Tokens.TokenList):
        self.tokens = tokens