import sys

import interpreter.lexer.tokenizer
import interpreter.tokens

def main():
    source_name = "impural/samples/fizzbuzz.im" #sys.argv[1]

    with open(source_name) as source_file:
        source_code = source_file.read()
    
    tokens: list = interpreter.lexer.tokenizer.tokenize(source_code)
    interpreter.tokens.output_token_list(tokens)

if __name__ == "__main__":
    main()