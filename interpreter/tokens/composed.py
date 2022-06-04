from interpreter.tokens import BaseToken, Name, ParenTokenList, BlockTokenList

class PureFunctionDef(BaseToken):
    def __init__(self, ftype: Name, name: Name, args: ParenTokenList, block: BlockTokenList):
        self.ftype = ftype
        self.name = name
        self.args = args
        self.block = block
    
    def __str__(self):
        return f"PureFunctionDef<{self.name}: {self.ftype}>"