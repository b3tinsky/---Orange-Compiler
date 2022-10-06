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
    'FLOAT',
    'BOOL',
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
        ID,
        DO,
        WHILE,
        INPUT,
        PRINT,
        IF,
        ELSE,
        INT,
        FLOAT,
        BOOL,
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
        CTEBOOL,
        CTEFLOAT,
        CTESTRING,
    }

    # Regular expression rules for tokens
    SEMICOLON = r'\;'
    COMMA = r'\,'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LCURLY = r'\{'
    RCURLY = r'\}'
    EQ = r'\=\='
    NEQ = r'\!\='
    GTE = r'\>\='
    LTE = r'\<\='
    AND = r'\&\&'
    OR = r'\|\|'
    ASSIGN = r'\='
    GT = r'\>'
    LT = r'\<'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    DIVIDE = r'\/'

    # String containing ignored characters between tokens
    ignore         = ' \t'
    ignore_comment = r'\#.*'
    
    # Rule definitions
    @_('True', 'False')
    def CTEBOOL(self,t):
        # t.value = bool(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

    @_(r'\-?\d*\.\d+')
    def CTEFLOAT(self,t):
        t.value = float(t.value)
        return t

    @_(r'\-?\d+')
    def CTEINT(self,t):
        t.value = int(t.value)
        return t


    @_(r'\"[\w\s&.\-!@#$%^&*()_+\-=\[\]{};\':\\|,.<>\/?]*\"')
    def CTESTRING(self,t):
        t.value = str(t.value[1:-1]) # Returns string without quotation marks
        return t

    # Reserved words
    ID['program'] = PROGRAM
    ID['vars']    = VARS
    ID['main']    = MAIN
    ID['func']    = FUNC
    ID['return']  = RETURN
    ID['void']    = VOID
    ID['from']    = FROM
    ID['to']      = TO
    ID['by']      = BY
    ID['do']      = DO
    ID['while']   = WHILE
    ID['input']   = INPUT
    ID['print']   = PRINT
    ID['if']      = IF
    ID['else']    = ELSE
    ID['int']     = INT
    ID['float']   = FLOAT
    ID['bool']    = BOOL
    
    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Error handling rule
    def error(self, t):
        self.index += 1
        raise lexicalError("❌ Illegal character '%s'" % t.value[0])
