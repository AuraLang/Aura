import sys

import interpreter.tokens as Tokens

import interpreter.lexer.tokenizer as Tokenizer

import interpreter.validation.expectation_checker as Expectations

import interpreter.ast.astbuilder as ASTBuilder

import interpreter.compilation.target as CompilationTarget
import interpreter.compilation.base_transpiler as BaseTranspiler

def main():
    # debug options, will use sys.argv for real
    source_name = "samples/fizzbuzz.im" # sys.argv[1]
    compilation_target = "python3" # sys.argv[2]

    # get source code from file
    with open(source_name) as source_file:
        source_code = source_file.read()
    
    # tokenize the source code
    tokens: Tokens.TokenList = Tokenizer.tokenize(source_code)
    print(tokens)

    # validate the tokenlist
    assert "This needs doing"
    isValid: bool = Expectations.isValid(tokens)

    if isValid:
        # build the AST
        assert "This needs doing"
        ast: ASTBuilder.AST = ASTBuilder.AST(tokens)
    
        # compile AST into target
        assert "This needs doing"
        target: type = CompilationTarget.getTarget(compilation_target)

        # run target transpiler
        assert "This needs doing"
        target.execute(ast)

if __name__ == "__main__":
    main()