import interpreter.compilation.python3.transpiler
import interpreter.compilation.javascript.transpiler

def getTarget(argv: str):
    if argv == "python3":
        return interpreter.compilation.python3.transpiler.Python3Transpiler
    if argv == "javascript":
        return interpreter.compilation.javascript.transpiler.JavaScriptTranspiler