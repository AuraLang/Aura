import interpreter.tokens as Tokens

class NestedTokenList:
    output_prefix: str = "\033[96m{\033[0m"
    output_suffix: str = "\033[36m}\033[0m"

    def __init__(self, parent=None):
        self.parent = parent
        self.inner = Tokens.TokenList()

        self.level = 0 if parent == None else parent.level + 1
    
    def append(self, token: Tokens.RawToken):
        self.inner.append(token)
    
    def __str__(self):
        return self.output_prefix + ' '.join(str(i) for i in self.inner) + self.output_suffix

class ParenTokenList(NestedTokenList):
    output_prefix: str = "\033[96m(\033[0m"
    output_suffix: str = "\033[96m)\033[0m"

class BlockTokenList(NestedTokenList):
    output_prefix: str = "\033[94m{\033[0m"
    output_suffix: str = "\033[94m}\033[0m"

def token_list_type(token: Tokens.RawToken):
    if token.__class__ == Tokens.IndentPlus:
        return BlockTokenList
    if token.__class__ == Tokens.OParen:
        return ParenTokenList

def matcher(tokens: Tokens.TokenList) -> NestedTokenList:
    stack: Tokens.TokenList = Tokens.TokenList()
    outer: NestedTokenList = NestedTokenList()
    pointer: NestedTokenList = outer

    for token in tokens:
        if hasattr(token, "_match_end"):
            stack.append(token._match_end)
            nested: NestedTokenList = token_list_type(token)(parent=pointer)
            pointer.append(nested)
            pointer = nested
        elif (stack[-1] if len(stack) else 0) == token.__class__:
            pointer = pointer.parent
        else:
            pointer.append(token)
    
    return outer