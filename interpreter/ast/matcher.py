import interpreter.tokens as Tokens

from interpreter.tokens import NestedTokenList, BlockTokenList, ParenTokenList

def token_list_type(token: Tokens.BaseToken):
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