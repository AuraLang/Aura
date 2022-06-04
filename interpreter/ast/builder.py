import interpreter.tokens as Tokens

from interpreter.ast.matcher import matcher
from interpreter.ast.composition import composition

token_patterns = {
    Tokens.PureFunctionDef: [Tokens.KWPure, Tokens.Name, Tokens.Name, Tokens.ParenTokenList, Tokens.BlockTokenList]
}

def check_pattern(token_list: Tokens.TokenList, index: int, pattern: list):
    if (index + len(pattern)) > len(token_list):
        return False
    
    for ind, elem in enumerate(pattern):
        ...

class AST:
    def __init__(self, tokens: Tokens.TokenList):
        self.tokens = tokens

        nested: Tokens.NestedTokenList = matcher(tokens)
        
        composed = composition(nested)