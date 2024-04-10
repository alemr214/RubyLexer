from tkinter import W
from reserved import reserved_words

# --------------------------------------------
#
#    Tokens for lexer
#
# --------------------------------------------
tokens = (
    # Data types
    "COMPLEX",
    "RATIONAL",
    "STRING",
    "INTEGER",
    "FLOAT",
    # Delimiters
    "L_PAREN",
    "R_PAREN",
    "L_BRACKET",
    "R_BRACKET",
    "L_BRACE",
    "R_BRACE",
    # Operators
    "ARITHMETIC_OPERATOR",
    "COMPARISON_OPERATOR",
    "LOGICAL_OPERATOR",
    "ASSIGNMENT_OPERATOR",
    "BITWISE_OPERATOR",
    "RANGE_OPERATOR",
    # Separators
    "COMMA",
    "COLON",
    "DOT",
    # Identifiers
    "RESERVED",
    "IDENTIFIER",
)
# --------------------------------------------
#
#    Simple Regex
#
# --------------------------------------------
t_L_PAREN = r"\("
t_R_PAREN = r"\)"
t_L_BRACKET = r"\["
t_R_BRACKET = r"\]"
t_L_BRACE = r"\{"
t_R_BRACE = r"\}"
t_COMMA = r"\,"
t_COLON = r"\:"
t_DOT = r"\."
# --------------------------------------------
#
#    Regex functions
#
# --------------------------------------------


def t_COMPLEX(t):
    r"(\d+\.\d+[iI])"
    t.type = "COMPLEX"
    return t


def t_RATIONAL(t):
    r"(\d+\/\d+)"
    t.type = "RATIONAL"
    return t


def t_STRING(t):
    r"(\"[^\"]*\")|(\'[^\']*\')"
    t.type = "STRING"
    return t


def t_INTEGER(t):
    r"\d+(?![\.\d])"
    t.type = "INTEGER"
    return t


def t_FLOAT(t):
    r"(\d+\.\d+)"
    t.type = "FLOAT"
    return t


def t_ARTIHMETIC_OPERATOR(t):
    r"(\+|\-|\*|\/|\%|\*\*)"
    t.type = "ARITHMETIC_OPERATOR"
    return t


def t_COMPARISON_OPERATOR(t):
    r"(\=\=|\!\=|\<|\>|\<\=|\>\=|\<\=\>|\=\=\=)"
    t.type = "COMPARISON_OPERATOR"
    return t


def t_LOGICAL_OPERATOR(t):
    r"(\&\&|\|\||\!)"
    t.type = "LOGICAL_OPERATOR"
    return t


def t_ASSIGNMENT_OPERATOR(t):
    r"(\=|\+=|\-=|\*=|\/=|\%=|\**=)"
    t.type = "ASSIGNMENT_OPERATOR"
    return t


def t_BITWISE_OPERATOR(t):
    r"(\&|\||\~|\^|\<<|\>>)"
    t.type = "BITWISE_OPERATOR"
    return t


def t_RANGE_OPERATOR(t):
    r"(\.\.|\.\.\.)"
    t.type = "RANGE_OPERATOR"
    return t


def t_RESERVED(t):
    r"[a-zA-Z_]\w*"
    if t.value in reserved_words:
        t.type = "RESERVED"
    else:
        t.type = "IDENTIFIER"
    return t


def t_COMMENT(t):
    r"\#.*"
    pass


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0] + ", in line: " + str(t.lexer.lineno))
    t.lexer.skip(1)
    raise Exception(
        "Error lexicografico.\n Por favor remueva el caracter invalido e intentelo de nuevo.\n Caracter invalido '%s'"
        % t.value[0]
        + ", en la linea: "
        + str(t.lexer.lineno)
    )
