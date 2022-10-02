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
        self.QM = OrangeQuadMachine(self.OFD, self.SC)                   # Orange Quadruple Machine
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
    @_('MAIN changecontext LPAREN RPAREN declareblock')
    def main_block(self, p):
        return p

    # Normal block
    @_('LCURLY blockcontent RCURLY')
    def block(self, p):
        return p
    
    # Block with variable declaration
    @_('LCURLY decvars blockcontent RCURLY')
    def declareblock(self, p):
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
        # DOC: Explain why an empty dictionary must be added if no variables are declared
        if (self.OFD.context == 'global'):
            self.OFD.addfunc(self.programName, 'prog', {})
        elif (self.OFD.context == 'main'):
            self.OFD.addfunc('main', 'main', {})
        else:
            functionType = p[-8][1]
            self.OFD.addfunc(self.OFD.context, functionType, {})
        return p

    # Individual variable declaration line
        # int variable ;
    @_('type decvar SEMICOLON')
    def decvar_line(self, p):
        self.OVT.addvartokenstream(p, self.OFD.context, {} if not self.OFD.dir else self.OFD.dir[self.programName])
        return p
    
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
    @_('VOID ID changecontext LPAREN params RPAREN declareblock')
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
    @_('empty', 'logic super_exp')
    def super_exp_aux(self, p):
        return p
    
        # Chained expression
    @_('expression super_exp_quadgen super_exp_aux')
    def super_exp(self, p):
        return p
    
    @_('AND', 'OR')
    def logic(self, p):
        self.QM.addOperator(p[0])
        return p
    
    @_('')
    def super_exp_quadgen(self, p):
        # If latest floor has something <- [['+', '/'], []]
        if self.QM.operators[-1]:
            prec = ['&&', '||']
            if self.QM.operators[-1][-1] in prec:
                self.QM.generateQuadruple()       
        return p

    # Expression
        # Single expression
    @_('empty', 'relation expression')
    def expression_aux(self, p):
        return p
    
        # Chained expression
    @_('exp expression_quadgen expression_aux')
    def expression(self, p):
        return p
    
    # Relational symbol
    @_('GT', 'LT', 'GTE', 'LTE', 'EQ', 'NEQ')
    def relation(self, p):
        self.QM.addOperator(p[0])
        return p
    
    @_('')
    def expression_quadgen(self, p):
        # If latest floor has something <- [['+', '/'], []]
        if self.QM.operators[-1]:
            prec = ['>', '<', '>=', '<=', '==', '!=']
            if self.QM.operators[-1][-1] in prec:
                self.QM.generateQuadruple()       
        return p

    # Exp
        # Single term
    @_('empty', 'exp_sign exp')
    def exp_aux(self, p):
        return p
        
        # Arithmetic exp
    @_('term exp_quadgen exp_aux')
    def exp(self, p):
        return p
    
    @_('PLUS', 'MINUS')
    def exp_sign(self, p):
        self.QM.addOperator(p[0])
        return p
    
    @_('')
    def exp_quadgen(self, p):
        # If latest floor has something <- [['+', '/'], []]
        if self.QM.operators[-1]:
            prec = ['+', '-']
            if self.QM.operators[-1][-1] in prec:
                self.QM.generateQuadruple()       
        return p
    
    # Term
        # Single factor
    @_('empty', 'term_sign term')
    def term_aux(self, p):
        return p
        
        # Arithmetic exp
    @_('factor term_quadgen term_aux')
    def term(self, p):
        return p
    
    @_('TIMES', 'DIVIDE')
    def term_sign(self, p):
        self.QM.addOperator(p[0])
        return p

    @_('')
    def term_quadgen(self, p):
        # If latest floor has something <- [['*', '-'], []]
        if self.QM.operators[-1]:
            prec = ['*', '/']
            if self.QM.operators[-1][-1] in prec:
                self.QM.generateQuadruple()       
        return p
    
    # Factor
        # Call variable
    @_('var')
    def factor(self, p):
        # p[0]    -> ('var', 'tmp_1')
        # p[0][1] -> 'tmp_1'
        id = p[0][1]
        
        # Add var name and type to operand stack in the Quadruple Machine
        self.QM.addOperand(id)
    
        return p
        
        # Call function
    @_('call')
    def factor(self, p):
        return p
        
        # Constant variable
    @_('varcte')
    def factor(self, p):
        # self.QM.addOperand(p[0])
        return p
        
    # Expression with parenthesis
    @_('LPAREN fakefloor super_exp RPAREN')
    def factor(self, p):
        # Simbolizes the end of a parenthesis
            # Removes the latest 'fake floor'
        self.QM.operators.pop()
        return p
    
    # 'Creates' a new operator 'context' to follow a correct
    # order of operations given their precedence (through parenthesis)
    @_('')
    def fakefloor(self, p):
        self.QM.operators.append([])
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

    # TODO: Finish while loop
    # While loop definition
    @_('WHILE saveposition LPAREN expression RPAREN openjumpslot block filljumps')
    def whileloop(self, p):
        return p
        
    # Variable value assignment
    @_('assignment_var assignment_sign expression SEMICOLON')
    def assignment(self, p):
        # If latest floor has something <- [['*', '-'], []]
        if self.QM.operators[-1]:
            prec = ['=']
            if self.QM.operators[-1][-1] in prec:
                self.QM.generateQuadruple()    
        return p

    @_('ASSIGN')
    def assignment_sign(self, p):
        self.QM.addOperator(p[0])
        return p
    
    @_('ID')
    def assignment_var(self, p):
        self.QM.addOperand(p[0])
        return p
        
    # Input variable values
    @_('INPUT LPAREN readaux RPAREN SEMICOLON')
    def read(self, p):
        return p
        
    @_('readvalue', 'readvalue COMMA readaux')
    def readaux(self, p):
        return p

    @_('var')
    def readvalue(self, p):
        self.QM.addOperand(p[0][1])          # To not break the internals of addOperand, add fluff
        self.QM.addOperand(('', ''))      # To not break the internals of addOperand, add fluff
        self.QM.addOperator('R')          # P stands for PRINT
        self.QM.generateQuadruple()       # This makes a print for each parameter (print('a', 'b', ...))        
        return p


    # Print variables and/or strings
    @_('PRINT LPAREN writeaux RPAREN SEMICOLON')
    def write(self, p):
        return p
        
    # Print a super expression and/or a string
    @_('writevalues COMMA writeaux', 'writevalues')
    def writeaux(self, p):
        return p

    # Print a super expression and/or a string
    @_('super_exp')
    def writevalues(self, p):
        self.QM.addOperand(('', ''))      # To not break the internals of addOperand, add fluff
        self.QM.addOperator('P')          # P stands for PRINT
        self.QM.generateQuadruple()       # This makes a print for each parameter (print('a', 'b', ...))        
        return p
    
    # Print a super expression and/or a string
    @_('CTESTRING')
    def writevalues(self, p):
        self.QM.addOperand((p[0], 'str')) # Constants are identified as (constant, type)
        self.QM.addOperand(('', ''))      # To not break the internals of addOperand, add fluff
        self.QM.addOperator('P')          # P stands for PRINT
        self.QM.generateQuadruple()       # This makes a print for each parameter (print('a', 'b', ...))

        return p

    # HACK: Copy structure for looping
    # Conditional statement    
    @_('IF LPAREN super_exp RPAREN openjumpslot block ELSE filljumps openjumpslot block filljumps')
    def condition(self, p):
        return p

    @_('IF LPAREN super_exp RPAREN openjumpslot block filljumps')
    def condition(self, p):
        return p

    @_('')
    def openjumpslot(self, p):
        # Opening slot for an IF
        if p[-1] == ')':    # if (condition) <WE ARE HERE> {statements}
            self.QM.addOperator('GOTOF')
            self.QM.addOperand(('', ''))
            self.QM.generateQuadruple()
            self.QM.jumps.append(self.QM.QuadrupleNumber)
            
        
        # Opening slot for an ELSE
        elif p[-2] == 'else':   # if (condition) {statements} ELSE filljumps <WE ARE HERE> {statements}
            self.QM.addOperator('GOTO')
            self.QM.addOperand(('', ''))
            self.QM.addOperand(('', ''))
            self.QM.generateQuadruple()
            self.QM.jumps.append(self.QM.QuadrupleNumber)


        return p
    
    @_('')
    def saveposition(self, p):
        self.QM.jumps.append(self.QM.QuadrupleNumber + 1)
        return p

    @_('')
    def filljumps(self, p):
        # When filling an ELSE statement, we have fill the previous jump AHEAD
        # of the current quadruple location, since the current location is a GOTO,
        # everything inside would be ignored (it would be a double jump)
        # print('🍫: ', p[-7])
        if p[-1] == 'else':
            self.QM.QuadrupleNumber+=1  # Update with position ahead
            self.QM.fillJumps()         # Fill previous quadruple with position ahead
            self.QM.QuadrupleNumber-=1  # Revert position back to normal
        
        elif p[-7] == 'while':
            # Generate GOTO quadruple that will return us to before the WHILE's condition
            self.QM.addOperator('GOTO')
            self.QM.addOperand(('', ''))
            self.QM.addOperand(('', ''))
            self.QM.generateQuadruple()
            
            # Fill the WHILE's condition (GOTOF) with position AFTER the GOTO we just created
            self.QM.fillJumps()         # Fill previous quadruple with position ahead
            
            # Fill the GOTO quadruple that will return us to before the WHILE's condition
            whileStartPosition = self.QM.jumps.pop()  # <- This is the position we left after reading the <WHILE> token
            currentPosition = self.QM.QuadrupleNumber # <
            self.QM.jumps.append(currentPosition)
            self.QM.QuadrupleNumber = whileStartPosition-1
            self.QM.fillJumps()
            self.QM.QuadrupleNumber = currentPosition


            # self.QM.QuadrupleNumber+=1  # Update with position ahead
            # self.QM.QuadrupleNumber-=1  # Revert position back to normal

        # Filling a normal IF statement <- GOTOF
        else:
            self.QM.fillJumps()
        return p



    # Constant variable
    @_('CTEINT')
    def varcte(self, p):
        self.QM.addOperand((p[0], 'int')) # Constants are identified as (constant, type)
        return (p[0], 'int')

    @_('CTEFLOAT')
    def varcte(self, p):
        self.QM.addOperand((p[0], 'float')) # Constants are identified as (constant, type)
        return (p[0], 'float')

    @_('CTEBOOL')
    def varcte(self, p):
        self.QM.addOperand((p[0], 'bool')) # Constants are identified as (constant, type)
        return (p[0], 'bool')
    
    # Available types
    @_('INT', 'FLOAT', 'BOOL')
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
        Pname = p[-1]
        self.programName = Pname
        self.OFD.programName = Pname
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
