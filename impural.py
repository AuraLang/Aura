import sys

import interpreter.lexer.tokenizer
import interpreter.tokens

def main():
    source_name = "samples/fizzbuzz.im" #sys.argv[1]

    with open(source_name) as source_file:
        source_code = source_file.read()
    
    tokens: list = interpreter.lexer.tokenizer.tokenize(source_code)
    print(tokens)

if __name__ == "__main__":
    main()