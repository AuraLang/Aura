from interpreter.tokens.keywords import *
from interpreter.tokens.operators import *
from interpreter.tokens.base import *

tokens_map = {
    "+": OPPlus,
    "-": OPMinus,
    "/": OPSlash,
    "*": OPAsterisk,
    "%": OPModulus,
    "->": OPPipeline,
    "=": OPAssign,
    "==": OPEquals,
    ">": OPGreaterThan,
    ">=": OPGreaterEquals,
    "<": OPLesserThan,
    "<=": OPLesserEquals,
    "!=": OPNotEquals,
    ".": OPPeriod,

    "pure": KWPure,
    "impure": KWImpure,
    "if": KWIf,
    "elif": KWElif,
    "else": KWElse,
    "for": KWFor,
    "return": KWReturn,
    "while": KWWhile,
}