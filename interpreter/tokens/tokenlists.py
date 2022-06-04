import interpreter.tokens as Tokens

class NestedTokenList(Tokens.TokenList):
    output_prefix: str = "\033[96m|_\033[0m"
    output_suffix: str = "\033[36m_|\033[0m"

    def __init__(self, parent=None):
        self.parent = parent
        self.inner = Tokens.TokenList()

        self.level = 0 if parent == None else parent.level + 1

        super().__init__()
    
    def append(self, token: Tokens.BaseToken):
        super().append(token)
    
    def __str__(self):
        return self.output_prefix + ' '.join(str(i) for i in self.inner) + self.output_suffix

class ParenTokenList(NestedTokenList):
    output_prefix: str = "\033[96m(\033[0m"
    output_suffix: str = "\033[96m)\033[0m"

class BlockTokenList(NestedTokenList):
    output_prefix: str = "\033[94m{\033[0m"
    output_suffix: str = "\033[94m}\033[0m"