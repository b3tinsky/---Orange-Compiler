from sly import Lexer
from Components.status import lexicalError

class OrangeLexer(Lexer):
    def __init__(self, status):
        self.StatusChecker = status

    reserved = (
    'PROGRAM',
    'VARS',
    'MAIN',
    'FUNC',
    'RETURN',
    'VOID',
    'FROM',
    'TO',
    'BY',
    'DO',
    'WHILE',
    'INPUT',
    'PRINT',
    'IF',
    'ELSE',
    'INT',
    'FLOAT'
    )

    # Set of token names
    tokens = {
        PROGRAM,
        VARS,
        MAIN,
        FUNC,
        RETURN,
        VOID,
        FROM,
        TO,
        BY,
        DO,
        WHILE,
        INPUT,
        PRINT,
        IF,
        ELSE,
        INT,
        FLOAT,
        ID,
        SEMICOLON,
        COMMA,
        LPAREN,
        RPAREN,
        LBRACKET,
        RBRACKET,
        LCURLY,
        RCURLY,
        ASSIGN,
        EQ,
        NEQ,
        GT,
        GTE,
        LT,
        LTE,
        AND,
        OR,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        CTEINT,
        CTEFLOAT,
        CTESTRING,
    }

    # Reserved Words
    PROGRAM = 'program'
    VARS = 'vars'
    MAIN = 'main'
    FUNC = 'func'
    RETURN = 'return'
    VOID = 'void'
    FROM = 'from'
    TO = 'to'
    BY = 'by'
    DO = 'do'
    WHILE = 'while'
    INPUT = 'input'
    PRINT = 'print'
    IF = 'if'
    ELSE = 'else'
    INT = 'int'
    FLOAT = 'float'

    # Regular expression rules for tokens
    SEMICOLON = r'\;'
    COMMA = r'\,'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LCURLY = r'\{'
    RCURLY = r'\}'
    ASSIGN = r'\='
    EQ = r'\=\='
    NEQ = r'\!\='
    GT = r'\>'
    GTE = r'\>\='
    LT = r'\<'
    LTE = r'\<\='
    AND = r'\&\&'
    OR = r'\|\|'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    DIVIDE = r'\/'

    # String containing ignored characters between tokens
    ignore         = ' \t'
    ignore_comment = r'\#.*'

    # Rule definitions
    @_(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def ID(self, t):
        return t

    @_(r'\-?\d*\.\d+')
    def CTEFLOAT(self,t):
        t.value = float(t.value)
        return t

    @_(r'\-?\d+')
    def CTEINT(self,t):
        t.value = int(t.value)
        return t

    @_(r'\".*\"')
    def CTESTRING(self,t):
        t.value = str(t.value[1:-1]) # Returns string without quotation marks
        return t

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Error handling rule
    def error(self, t):
        self.index += 1
        raise lexicalError("❌ Illegal character '%s'" % t.value[0])
