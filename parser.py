# ▲▼

from sly import Parser
from lex import OrangeLexer

class OrangeParser(Parser):
    # Initiate without an error
    status = '✅'
    tokens = OrangeLexer.tokens

    ### GRAMMAR ###
    
    # Program declaration
    @_('PROGRAM ID declare')
    def program(self, p):
        return p

    # Declaration blocks (global variables & functions)
    @_('decvars decfuncs main_block')
    def declare(self, p):
        return p
    
    # Main program block
    @_('MAIN LPAREN RPAREN block')
    def main_block(self, p):
        return p

    # Normal block
    @_('LCURLY blockcontent RCURLY')
    def block(self, p):
        return p
    
    # Block with a value return
    @_('LCURLY blockcontent RETURN factor SEMICOLON RCURLY')
    def returnblock(self, p):
        return p

        # Single or multiple block content
    @_('statute', 'statute blockcontent', 'empty')
    def blockcontent(self, p):
        return p
    


    # (Optional)
    # Variable declaration block
    @_('VARS decvar_line', 'empty')
    def decvars(self, p):
        return p

    # Individual variable declaration line
        # int variable ;
    @_('type decvar SEMICOLON')
    def decvar_line(self, p):
        return p
    
    # Multiple variable declaration line
        # int variable ;
        # float x, y, z ;
    @_('type decvar SEMICOLON decvar_line')
    def decvar_line(self, p):
        return p
    
    # Individual variable
        # x
    @_('var')
    def decvar(self, p):
        return p
    
    # Multiple variables
        # x, y, z
    @_('var COMMA decvar')
    def decvar(self, p):
        return p
    
    # Normal variable
    @_('ID')
    def var(self, p):
        return p
    
    # Array variable
    @_('ID LBRACKET exp RBRACKET')
    def var(self, p):
        return p
    
    # Matrix variable
    @_('ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET')
    def var(self, p):
        return p


    # (Optional)
    # Function declaration block
    @_('func decfuncs', 'empty')
    def decfuncs(self, p):
        return p

    # Function type definition
    @_('FUNC voidfunc', 'FUNC typefunc')
    def func(self, p):
        return p

    # Function without a return value
        # void fullname(firstname, lastname) {
        #   print("Fullname: ", firstname, " ", lastname)
        # }
    @_('VOID ID LPAREN params RPAREN block')
    def voidfunc(self, p):
        return p

    # Function with a return value
        # int sum(a, b) {
        #   return a + b
        # }
    @_('type ID LPAREN params RPAREN returnblock')
    def typefunc(self, p):
        return p

    # Parameter declaration
        # Function()
        # Function(parameter)
        # Function(param1, param2, param3)
    @_('type ID', 'type ID COMMA params', 'empty')
    def params(self, p):
        return p

    # Function call
        # sum(2, 2)
        # fullname("Beto", "Rendon")
    @_('ID LPAREN callvalues RPAREN')
    def call(self, p):
        return p
    
    # Call values
        # func(2)
        # func(2, a + 1)
        # func()
    @_('exp', 'exp COMMA callvalues', 'empty')
    def callvalues(self, p):
        return p

    # Super Expression (logical)
        # Single expression
    @_('expression')
    def super_exp(self, p):
        return p
    
        # Chained expression
    @_(
        'expression AND super_exp',
        'expression OR super_exp',
    )
    def super_exp(self, p):
        return p
    
    # Expression
        # Single expression
    @_('exp')
    def expression(self, p):
        return p
    
        # Chained expression
    @_('exp relation exp')
    def expression(self, p):
        return p
    
    # Relational symbol
    @_('GT', 'LT', 'GTE', 'LTE', 'EQ', 'NEQ')
    def relation(self, p):
        return p
    
    # Exp
        # Single term
    @_('term')
    def exp(self, p):
        return p
        
        # Arithmetic exp
    @_(
        'term PLUS exp',
        'term MINUS exp',
    )
    def exp(self, p):
        return p
    
    # Term
        # Single factor
    @_('factor')
    def term(self, p):
        return p
        
        # Arithmetic exp
    @_(
        'factor TIMES term',
        'factor DIVIDE term',
    )
    def term(self, p):
        return p
    
    
    # Factor
        # Call variable
    @_('var')
    def factor(self, p):
        return p
        
        # Call function
    @_('call')
    def factor(self, p):
        return p
        
        # Constant variable
    @_('varcte')
    def factor(self, p):
        return p
        
        # Expression with parenthesis
    @_('LPAREN super_exp RPAREN')
    def factor(self, p):
        return p
        
    # For loop definition
        # Without step increments
    @_('FROM var ASSIGN expression TO expression DO block')
    def forloop(self, p):
        return p
        
        # With step increments
    @_('FROM var ASSIGN expression TO expression BY expression DO block')
    def forloop(self, p):
        return p
        
    # While loop definition
    @_('WHILE LPAREN expression RPAREN block')
    def whileloop(self, p):
        return p
        
    # Variable value assignment
    @_('ID ASSIGN expression SEMICOLON')
    def assignment(self, p):
        return p
        
    # Input variable values
    @_('INPUT LPAREN decvar RPAREN SEMICOLON')
    def read(self, p):
        return p
        
    # Print variables and/or strings
    @_('PRINT LPAREN writevalues RPAREN SEMICOLON')
    def write(self, p):
        return p
        
    # Print a super expression and/or a string
    @_('super_exp', 'CTESTRING', 'super_exp COMMA writevalues', 'CTESTRING COMMA writevalues')
    def writevalues(self, p):
        return p

    # Conditional statement    
    @_('IF LPAREN expression RPAREN block', 'IF LPAREN expression RPAREN block ELSE block')
    def condition(self, p):
        return p
    
    # Constant variable
    @_('CTEINT', 'CTEFLOAT')
    def varcte(self, p):
        return p
    
    # Available types
    @_('INT', 'FLOAT')
    def type(self, p):
        return p
        
    # Statute definition
    @_('assignment', 'condition', 'write', 'read', 'whileloop', 'forloop', 'var', 'call')
    def statute(self, p):
        return p
        
    @_('')
    def empty(self, p):
        pass

    def error(self, p):
        # print("Whoa. You are seriously hosed.")
        self.syntax_error = '❌'

        if not p:
            print("End of File!")
            return

        # Read ahead looking for a closing '}'
        while True:
            tok = next(self.tokens, None)
            if not tok or tok.type == 'RCURLY':
                break
        self.restart()

    # TODO: Define special functions
    # <specialfuncs>
        # mean
        # mode
        # variance
        # histogram
        # random
        # choice
