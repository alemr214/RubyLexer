# --------------------------------------------
#
#    Reserved words for lexer
#
# --------------------------------------------
reserved = {
    # Control flow
    "begin": "BEGIN",
    "end": "END",
    "case": "CASE",
    "else": "ELSE",
    "elsif": "ELSIF",
    "if": "IF",
    "unless": "UNLESS",
    "until": "UNTIL",
    "when": "WHEN",
    "while": "WHILE",
    "for": "FOR",
    "do": "DO",
    "next": "NEXT",
    "break": "BREAK",
    "redo": "REDO",
    "retry": "RETRY",
    "return": "RETURN",
    "yield": "YIELD",
    "rescue": "RESCUE",
    "ensure": "ENSURE",
    "in": "IN",
    # Logical operators
    "true": "TRUE",
    "false": "FALSE",
    "nil": "NIL",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    # Object handling
    "class": "CLASS",
    "module": "MODULE",
    "def": "DEF",
    "self": "SELF",
    "super": "SUPER",
    "new": "NEW",
    "alias": "ALIAS",
    "defined": "DEFINED",
    "undef": "UNDEF",
    # Data structures
    "Set": "SET",
    "Hash": "HASH",
    "Matrix": "MATRIX",
    "then": "THEN",
    # Input/Output
    "puts": "PUTS",
    "print": "PRINT",
    "gets": "GETS",
}

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
    # Separators
    "COMMA",
    "COLON",
    "SEMICOLON",
    # Identifiers
    "OPERATOR",
    "RESERVED",
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
t_SEMICOLON = r"\;"

# --------------------------------------------
#
#    Regex functions
#
# --------------------------------------------


def t_OPERATOR(t):
    r"(\+|\-|\*|\/|\%|\^|\&|\||\~|\!|\=|\<|\>|\?|\:|\$|\@|\\|\`|\,|\;|\[|\]|\{|\}|\(|\)|\.)"
    return t
