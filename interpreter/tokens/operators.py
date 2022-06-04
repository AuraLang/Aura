from interpreter.tokens.base import BaseToken

class RawOperator(BaseToken):
    details = None

class OPPlus(RawOperator):
    symbol = "+"

class OPMinus(RawOperator):
    symbol = "-"

class OPSlash(RawOperator):
    symbol = "/"

class OPAsterisk(RawOperator):
    symbol = "*"

class OPModulus(RawOperator):
    symbol = "%"

class OPPipeline(RawOperator):
    symbol = "->"

class OPAssign(RawOperator):
    symbol = "="

class OPEquals(RawOperator):
    symbol = "=="

class OPGreaterThan(RawOperator):
    symbol = ">"

class OPLesserThan(RawOperator):
    symbol = "<"

class OPGreaterEquals(RawOperator):
    symbol = ">="

class OPLesserEquals(RawOperator):
    symbol = "<="

class OPNotEquals(RawOperator):
    symbol = "!="

class OPPeriod(RawOperator):
    symbol = "."

class CParen(BaseToken):
    ...

class OParen(BaseToken):
    _match_end = CParen