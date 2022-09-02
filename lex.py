from ply.lex import lex

class OrangeLexer():
    # Reserved Words
    reserved = {
        'program': 'PROGRAM',
        'vars'   : 'VARS',
        'main'   : 'MAIN',
        'func'   : 'FUNC',
        'return' : 'RETURN',
        'void'   : 'VOID',
        'from'   : 'FROM',
        'to'     : 'TO',
        'by'     : 'BY',
        'do'     : 'DO',
        'while'  : 'WHILE',
        'input'  : 'INPUT',
        'print'  : 'PRINT',
        'if'     : 'IF',
        'else'   : 'ELSE',
        'int'    : 'INT',
        'float'  : 'FLOAT',
        'id'  : 'ID',
    }

    # List of token names
    tokens = [
        'SEMICOLON',
        'COLON',
        'COMMA',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'LCURLY',
        'RCURLY',
        'ASSIGN',
        'EQ',
        'NEQ',
        'GT',
        'GTE',
        'LT',
        'LTE',
        'AND',
        'OR',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'CTEINT',
        'CTEFLOAT',
        'CTESTRING',
    ] + list(reserved.values())

    # Regular expression rules for tokens
    t_SEMICOLON = r'\;'
    t_COLON = r'\:'
    t_COMMA = r'\,'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LCURLY = r'\{'
    t_RCURLY = r'\}'
    t_ASSIGN = r'\='
    t_EQ = r'\=\='
    t_NEQ = r'\!\='
    t_GT = r'\>'
    t_GTE = r'\>\='
    t_LT = r'\<'
    t_LTE = r'\<\='
    t_AND = r'\&\&'
    t_OR = r'\|\|'
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'\/'

    # Rule definitions
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')
        # if t.value in self.keywords:
        #     t.type = self.keywords.get(t.value,'ID')    # Check for reserved words
        return t

    def t_CTEFLOAT(self,t):
        r'\-?\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_CTEINT(self,t):
        r'\-?\d+'
        t.value = int(t.value)
        return t

    def t_CTESTRING(self,t):
        r'\".*\"'
        t.value = str(t.value[1:-1]) # Returns string without quotation marks
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    # Define a rule for comments
    def t_comment(self, t):
        r'\#.*'
        pass

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # A string containing ignored characters (spaces and tabs)
    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)


        # Test the data
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            # print(tok.type, tok.value, tok.lineno)
            print(tok)
    
    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex(module=self, **kwargs)
        return self.lexer
