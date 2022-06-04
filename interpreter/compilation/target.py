import interpreter.compilation.python3.transpiler

def getTarget(argv: str):
    if argv == "python3":
        return interpreter.compilation.python3.transpiler.Python3Transpiler