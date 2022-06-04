import interpreter.tokens as Tokens

from interpreter.ast.matcher import matcher, NestedTokenList

class AST:
    def __init__(self, tokens: Tokens.TokenList):
        self.tokens = tokens

        nested: NestedTokenList = matcher(tokens)
        print(nested)