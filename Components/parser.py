# ▲▼

from sly import Parser
from Components.scanner import OrangeLexer
# DOC: Explain why I need a deep copy instead of using the same VariableTable object
    # I need a copy because every context switch "whipes" the table, but the address remains
    # With a copy an entirely new table is stored for its current context/scope/directory 
# from copy import deepcopy as COPY
from Components.funcdir import OrangeFuncDir
from Components.vartable import OrangeVarTable
from Components.status import syntacticalError
from Components.semcube import OrangeCube
from Components.quadmachine import OrangeQuadMachine

class OrangeParser(Parser):
    tokens = OrangeLexer.tokens
    debugfile = 'parser.out'    # Parser debugging file
    start = 'program'           # Start parsing from < program > rule
    reserved = OrangeLexer.reserved
    
    def __init__(self, status):
        self.StatusChecker = status   # Initiate status checker
        self.OFD = OrangeFuncDir(self.StatusChecker)    # Orange Function Directory
        self.OVT = OrangeVarTable(self.StatusChecker)   # Orange Variable Table
        self.SC = OrangeCube()                          # Orange Semantic Cube
        self.QM = OrangeQuadMachine()                   # Orange Quadruple Machine
        self.programName = ''

    ### GRAMMAR ###
    
    # Program declaration
    @_('PROGRAM ID saveprogramname declare')
    # @_('PROGRAM ID declare')
    def program(self, p):

        return p

    # Declaration blocks (global variables & functions)
    # @_('decvars saveglobalvars decfuncs main_block')
    @_('decvars decfuncs main_block')
    def declare(self, p):
        return p

    # Main program block
    @_('MAIN changecontext LPAREN RPAREN block')
    def main_block(self, p):
        return p

    # Normal block
    @_('LCURLY decvars blockcontent RCURLY')
    def block(self, p):
        return p
    
    # WARNING: Changed RETURN factor to RETURN exp
        # Did this so I could return things like a + b instead of (a + b)
    # Block with a value return
    @_('LCURLY decvars blockcontent RETURN exp SEMICOLON RCURLY')
    def returnblock(self, p):
        return p

        # Single or multiple block content
    @_('statute blockcontent', 'empty')
    def blockcontent(self, p):
        return p
    


    # (Optional)
    # Variable declaration block
    @_('VARS decvar_line')
    def decvars(self, p):
        if self.OFD.context == 'global':
            self.OFD.addfunc(self.programName, 'prog', self.OVT.table)

        elif self.OFD.context == 'main':
            self.OFD.addfunc('main', 'main', self.OVT.table)
        else:
            # If its a typed function it returns a tuple like ('type', 'int')
            if isinstance(p[-9], tuple):
                functionType = p[-9][1]
            
            # Otherwise it only returns a 'VOID' string
            else:
                functionType = p[-9]

            self.OFD.addfunc(self.OFD.context, functionType, self.OVT.table)
        return p

    @_('empty')
    def decvars(self, p):
        if (self.OFD.context == 'global'):
            self.OFD.addfunc(self.programName, 'prog', {})
        return p

    # FIXME: Declaring variables don't require checking for global vars
    # Individual variable declaration line
        # int variable ;
    @_('type decvar SEMICOLON')
    def decvar_line(self, p):
        self.OVT.addvartokenstream(p, self.OFD.context, {} if not self.OFD.dir else self.OFD.dir[self.programName])
        return p
    
    # FIXME: Declaring variables don't require checking for global vars
    # Multiple variable declaration line
        # int variable ;
        # float x, y, z ;
    @_('type decvar SEMICOLON decvar_line')
    def decvar_line(self, p):
        self.OVT.addvartokenstream(p, self.OFD.context, {} if not self.OFD.dir else self.OFD.dir[self.programName])
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
    @_('ID LBRACKET CTEINT RBRACKET')
    def var(self, p):
        return p
    
    # Matrix variable
    @_('ID LBRACKET CTEINT RBRACKET LBRACKET CTEINT RBRACKET')
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
    @_('VOID ID changecontext LPAREN params RPAREN block')
    def voidfunc(self, p):
        return p

    # Function with a return value
        # int sum(a, b) {
        #   return a + b
        # }
    @_('type ID changecontext LPAREN params RPAREN returnblock')
    def typefunc(self, p):
        # In second argument add p[0] -> whatever < type > returns
        # Add p[0][1] to get the second element -> < type > returns tuples like ('type', 'int')
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
        # p[0]    -> ('var', 'tmp_1')
        # p[0][1] -> 'tmp_1'
        
        # id = p[0][1]
        # HACK: Add the checkVar to genQuad, so only one function gets called
        # TODO: Check variable in current context and global scope
        # self.OFD.checkVar(id)
        # TODO: Add quadruple

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
    @_('assignment', 'condition', 'write', 'read', 'whileloop', 'forloop', 'call')
    def statute(self, p):
        return p
    
    ### HELPER RULES ###
    # Changes context BEFORE entering the new block
        # Usually the context changes AFTER the rule is finished, but this doesn't work for variable tables  
    @_('')
    def changecontext(self, p):
        self.OVT.cleartable()
        if (p[-2] == 'program'):
            self.OFD.changeContext('global')
        else:
            self.OFD.changeContext(p[-1])
    
    # DOC: Save the program name ASAP to identify repeated variable & function names
    @_('')
    def saveprogramname(self, p):
        # Save program name to check for global variables later
        self.programName = p[-1]
        # Return the ID again so that global declare block can have a name
            # If not returned, the declare block takes p[-1], which would be 
            # whatever we return here (or not)
        return p[-1]

    @_('')
    def empty(self, p):
        pass

    def error(self, p):
        # print("Whoa. You are seriously hosed.")
        
        if not p:
            raise syntacticalError("❌ End of File!")
            # return

        raise syntacticalError(f'❌ Syntax error: [{p.type} -> {p.value}] before or at line {p.lineno} position {p.index}')
        # Read ahead looking for a closing '}'
        # while True:
        #     tok = next(self.tokens, None)
            
        #     if not tok or tok.type == 'RCURLY':
        #         print(f'❌ SYNTAX ERROR: Missing [Closing brace -> {tok.value}] before line {p.lineno} position {p.index}')
        #         break
            
        #     elif not tok or tok.type == 'SEMICOLON':
        #         print(f'❌ SYNTAX ERROR: Missing [{tok.type} -> {tok.value}] before line {p.lineno} position {p.index}')
        #         break

        #     else:
        #         print(f'Syntax error: [{p.type} -> {p.value}] before line {p.lineno} position {p.index}')
        #         break

            # self.errok()
            # self.restart()
        # self.restart()
        # return tok

    # TODO: Define error rules
    # Reserved words cannot be used as variable IDs
        # The * is because SLY need the values UNPACKED instead of the tuple/list/dict
    @_(*reserved)
    def var(self, p):
        raise syntacticalError('❌ Variables cannot be identified as a reserved word')
    

    # TODO: Define special functions
    # <specialfuncs>
        # mean
        # mode
        # variance
        # histogram
        # random
        # choice
