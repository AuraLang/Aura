import re
import sys

# exports
def tokenize(code: str):
    return Reader().read(code).tokens

# not exports

import interpreter.tokens as T

class Reader:
    punctuation: str = "+-*/.=<>,%!"
    alphanumeric: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"

    def chartype(char: str):
        if char in Reader.punctuation:
            return "punct"
        if char in Reader.alphanumeric:
            return "alpha"

    def __init__(self):
        self.acc: str = ""
        self.tokens: str = T.TokenList()

        self.strmode: bool = False
        self.stropen: str = ""

        self.justnewlined: bool = False
        self.currentstyle: str = ""
        self.indentlevel: int = 0

        self.linenumber: int = 0
    
    def get_token_type(self, token: str):
        specials: dict = {
            "\n": T.NewLine,
            "(": T.OParen,
            ")": T.CParen
        }
        if token in specials:
            return specials[token]()

        if re.fullmatch('\d+(.\d+)?', token):
            return T.LiteralNum(token)
        
        if token[0] == token[-1] == '"':
            return T.LiteralStr(token)
        
        if re.fullmatch('\w+', token):
            return T.Name(token)
        
        if token in ["+", "-", "*", "/", "%", "->", "!=", "==", ">", "<", ">=", "<=", "=", "."]:
            return T.Operator(token)

        return token

    def pushacc(self):
        if self.justnewlined:
            self.linenumber += 1
            if " " in self.acc and "\t" in self.acc:
                print(f"\033[31mLine {self.linenumber}: Mismatched tabs and spaces\033[0m")
                sys.exit()

            if self.acc == self.indentlevel * self.currentstyle:
                pass

            elif self.indentlevel == 0 and self.acc != "":
                self.currentstyle = self.acc
                self.indentlevel += 1
                self.tokens.append(T.IndentPlus())

            elif self.acc == ((self.indentlevel + 1) * self.currentstyle):
                self.indentlevel += 1
                self.tokens.append(T.IndentPlus())
            
            elif (lacc := len(self.acc)) < (lind := len((self.indentlevel) * self.currentstyle)):
                diff: int = int(lacc / len(self.currentstyle) - lind / len(self.currentstyle))
                self.indentlevel += diff
                self.tokens += [T.IndentMinus()] * -diff

            self.previndent = self.acc
            self.acc = ""
            return

        if self.acc != "":
            self.tokens.append(self.get_token_type(self.acc))
            self.acc = ""

    def readchar(self, char: str, prev: str):
        if self.strmode:
            if char == self.stropen:
                self.acc += '"'
                self.pushacc()
                self.strmode = False
                return
            else:
                self.acc += char
                return

        if char in ["'", '"']:
            self.pushacc()
            self.acc += '"'
            self.strmode = True
            self.stropen = char
            return

        if char in "}()[]{":
            self.pushacc()
            self.acc = char
            self.pushacc()
            return

        if self.justnewlined:
            if char in (" " + "\t"):
                self.acc += char
                return
            self.pushacc()
            self.justnewlined = False

        if char == "\n":
            self.pushacc()
            self.acc = "\n"
            self.pushacc()
            self.justnewlined = True
            return

        if char == " ":
            self.pushacc()
            return

        if Reader.chartype(char) != Reader.chartype(prev):
            self.pushacc()
            self.acc += char
            return

        self.acc += char

    def read(self, code: str):
        prev: str = ""
        code = code + "\nend"
        for char in code:
            self.readchar(char, prev)
            prev = char
        return self