import sys

import interpreter

def main():
    source_name = sys.argv[1]

    with open(source_name) as source_file:
        source_code = source_file.read()
    
    tokens: list = interpreter.lexer.tokenizer.tokenize(source_code)

if __name__ == "__main__":
    main()