import interpreter.tokens as Tokens

from interpreter.tokens import NestedTokenList
from interpreter.validation.patterns import checkExists

def composition(tokens: NestedTokenList):
    res: NestedTokenList = NestedTokenList()

    enumerator = enumerate(tokens)

    for index, elem in enumerator:
        if checkExists:
            raise Exception("Stupid code is still here, fix now.")
        # TEMPORARY :: REDO WHEN PATTERN MATCHING IS DONE

        if (index + 6) < len(tokens):
            print(" ".join([i.__class__.__name__ for i in tokens[index:index+5]]))
            if (
                tokens[index].__class__ == Tokens.KWPure and
                tokens[index+1].__class__ == Tokens.Name and
                tokens[index+2].__class__ == Tokens.Name and
                tokens[index+3].__class__ == Tokens.ParenTokenList and
                tokens[index+4].__class__ == Tokens.NewLine and
                tokens[index+5].__class__ == Tokens.BlockTokenList
            ):
                print("Pure Function Detected Without Args!")
                print(Tokens.PureFunctionDef(
                    *tokens[index+1:index+5]
                ))
                res.append(Tokens.PureFunctionDef(
                    *tokens[index+1:index+5]
                ))
                #for _ in range(5): next(enumerator)
        else:
            print("append", elem)
            res.append(elem)
    
    print(res)