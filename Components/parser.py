# ▲▼

import pickle
from sly import Parser
from Components.scanner import OrangeLexer
# DOC: Explain why I need a deep copy instead of using the same VariableTable object
    # I need a copy because every context switch "whipes" the table, but the address remains
    # With a copy an entirely new table is stored for its current context/scope/directory 
# from copy import deepcopy as COPY
from Components.funcdir import OrangeFuncDir
from Components.vartable import OrangeVarTable
from Components.status import semanticError, syntacticalError
from Components.semcube import OrangeCube
from Components.quadmachine import OrangeQuadMachine


class OrangeParser(Parser):
    tokens = OrangeLexer.tokens
    debugfile = 'parser.out'    # Parser debugging file
    start = 'program'           # Start parsing from < program > rule
    reserved = OrangeLexer.reserved
    
    def __init__(self, status, memory):
        self.StatusChecker = status   # Initiate status checker
        self.MM  = memory   # Initiate status checker
        self.OFD = OrangeFuncDir(self.StatusChecker, self.MM)    # Orange Function Directory
        self.OVT = OrangeVarTable(self.StatusChecker, self.MM)   # Orange Variable Table
        self.SC  = OrangeCube()                         # Orange Semantic Cube
        self.QM  = OrangeQuadMachine(self.OFD, self.SC, self.MM) # Orange Quadruple Machine
        self.programName = ''

    ### GRAMMAR ###
    
    # Program declaration
    @_('PROGRAM ID saveprogramname declare')
    def program(self, p):
        with open('ovejota.pickle','wb') as obj:
            DUMP = {
                'quadruples': self.QM.quadruples,
                'functiondirectory': self.OFD.dir,
                'constantstable': self.OFD.constants,
                'programname': self.OFD.programName
            }
            pickle.dump(DUMP, obj)
        return p

    # Declaration blocks (global variables & functions)
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
    
    # Single or multiple block content
    @_('statute blockcontent', 'empty')
    def blockcontent(self, p):
        return p
    
    # (Optional)
    # Variable declaration block
    @_('VARS decvar_line')
    def decvars(self, p):
        if self.OFD.context == self.programName:
            self.OFD.dir[self.programName]['table'] = self.OVT.table

        elif self.OFD.context == 'main':
            self.OFD.dir['main']['table'] = self.OVT.table
        
        else:
            self.OFD.dir[self.OFD.context]['table'] = self.OVT.table

        # When variable declaration ends, add quadruple number to function
        self.OFD.dir[self.OFD.context]['quadruple'] = self.QM.QuadrupleNumber

        return p

    @_('empty')
    def decvars(self, p):
        return p

    # Individual variable declaration line
        # int variable ;
    @_('decvar_type decvar SEMICOLON')
    def decvar_line(self, p):
        self.OVT.addvartokenstream(p, self.OFD.context, {} if not self.OFD.dir else self.OFD.dir[self.programName])
        return p
    
    # Multiple variable declaration line
        # int variable ;
        # float x, y, z ;
    @_('decvar_type decvar SEMICOLON decvar_line')
    def decvar_line(self, p):
        self.OVT.addvartokenstream(p, self.OFD.context, {} if not self.OFD.dir else self.OFD.dir[self.programName])
        return p
    
    @_('type')
    def decvar_type(self, p):
        self.OVT.varType = p[0][1]
        return p[0]

    # Individual variable
        # x
    @_('var')
    def decvar(self, p):
        # Keep track of size needed for local variables
        if self.OFD.context == self.programName:
            functionName = self.programName
        else:
            functionName = self.OFD.context

        self.OFD.dir[functionName]['size']['local'][self.OVT.varType] += 1

        return p
    
    # Multiple variables
        # x, y, z
    @_('var COMMA decvar')
    def decvar(self, p):
        if self.OFD.context == self.programName:
            functionName = self.programName
        else:
            functionName = self.OFD.context
        
        # Keep track of size needed for local variables
        self.OFD.dir[functionName]['size']['local'][self.OVT.varType] += 1

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
        # Function without a return value
            # void fullname(firstname, lastname) {
            #   print("Fullname: ", firstname, " ", lastname)
            # }
        # Function with a return value
            # int sum(a, b) {
            #   return a + b
            # }
    @_('FUNC functype ID changecontext LPAREN params RPAREN declareblock')
    def func(self, p):
        # In second argument add p[0] -> whatever < type > returns
        # Add p[0][1] to get the second element -> < type > returns tuples like ('type', 'int')
        self.QM.addOperator('ENDFUNC')
        self.QM.addOperand((-1, -1))
        self.QM.addOperand((-1, -1))
        self.QM.generateQuadruple()
        return p
    
    @_('VOID')
    def functype(self, p):
        return p[0]
    
    @_('type')
    def functype(self, p):
        return p[0]

    # Parameter declaration
    @_('param params_aux', 'empty')
    def params(self, p):
        return p

    @_('type ID')
    def param(self, p):
        paramType = p[0][1]
        paramName = p[1]
        self.OFD.addParam(paramName, paramType)
        return p

    @_('COMMA params','empty')
    def params_aux(self, p):
        return p

    # Function call
        # sum(2, 2)
        # fullname("Beto", "Rendon")
    @_('ID generate_era LPAREN callvalues RPAREN')
    def call(self, p):
        if self.QM.CallSignature != self.OFD.dir[p[0]]['signature']:
            raise semanticError(f"❌ Function signature mismatch | Arguments given for < {self.OFD.dir[p[0]]['name']} > do not match the function's signature")
        else:
            # This means the call is for a typed function, meaning it needs to add the global
            # variable to store the function's result
            nonReturnTypes = ['main', 'void', 'prog']
            if self.OFD.dir[p[0]]['type'] not in nonReturnTypes:
                self.QM.addOperand(p[0])
            
            # Generate GOSUB quadruple
            self.QM.addOperator('GOSUB')
            self.QM.addOperand((p[0], 'func'))
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()

            # Reset parameter counter
            self.QM.ParameterNumber = 0
        return p
    
    @_('')
    def generate_era(self, p):
        # Reset parameter counter and signature
        self.QM.ParameterNumber = 0
        self.QM.CallSignature   = ''

        # Check if function exists
        if self.OFD.checkfunc(p[-1]):

            # Generate Activation Record Expansion -new- size quadruple
            self.QM.addOperator('ERA')
            self.QM.addOperand((p[-1], 'func'))
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()
        
        # Raise error if function doesn't exist
        else:
            raise semanticError(f'❌ Function < {p[-1]} > does not exist')

        return p
    
    # Call values
        # func(2)
        # func(2, a + 1)
        # func()
    @_('empty', 'COMMA callvalues')
    def callvalues_aux(self, p):
        return p

    @_('exp generate_param callvalues_aux')
    def callvalues(self, p):

        return p
    
    @_('')
    def generate_param(self, p):
        self.QM.CallSignature += self.QM.operands[-1][1][0]
        self.QM.addOperator('PARAM')
        paramNum = self.QM.generateParameter()
        self.QM.addOperand((paramNum,'param'))
        self.QM.generateQuadruple()
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
    @_('FROM forloopcontrolvar assignment_sign expression validatecontrolvar TO createfinaltempvar expression validateloopend DO openjumpslot block filljumps')
    def forloop(self, p):
        return p
 
    @_('var')
    def forloopcontrolvar(self, p):
        # p[0]    -> ('var', 'tmp_1')
        # p[0][1] -> 'tmp_1'
        id = p[0][1]
        
        # Add var name and type to operand stack in the Quadruple Machine
        varName, varType = self.OFD.checkVar(id)
        if varType == 'int':
            self.QM.addOperand(id)

        else:
            raise semanticError('❌ Type mismatch | Control variable in FOR loop must be an integer')
            
        return p
    
    @_('')
    def validatecontrolvar(self, p):
        self.QM.generateQuadruple()
        return p

    @_('')
    def createfinaltempvar(self, p):
        vfinalName = (self.QM.generateTempVar('int'), 'int')
        self.QM.operands.append(vfinalName)
        # self.QM.addOperand(vfinalName)
        return p

    @_('')
    def validateloopend(self, p):
        if self.QM.operands[-1][1] == 'int':
            # Assign expression to tempfinalvar
            self.QM.addOperator('=')
            self.QM.generateQuadruple()

            # Create comparison quadruple
            controlVariable = (self.QM.quadruples[self.QM.QuadrupleNumber-2][3], 'int')
            endVariable     = (self.QM.quadruples[self.QM.QuadrupleNumber-1][3], 'int')
            self.QM.addOperator('<')
            
            # Add operands directly (with addOperand() it adds the addresses as constants)
            self.QM.operands.append(controlVariable)
            self.QM.operands.append(endVariable)

            self.QM.generateQuadruple()
            self.QM.jumps.append(self.QM.QuadrupleNumber)

        else:
            raise semanticError('❌ Type mismatch | FOR loop ending must be an integer')

            # return p
    




    
    # HACK: Add a custom increment
        # With step increments
    # @_('FROM var ASSIGN expression TO expression BY expression DO block')
    # def forloop(self, p):
    #     return p

    # While loop definition
    @_('WHILE saveposition LPAREN expression RPAREN openjumpslot block filljumps')
    def whileloop(self, p):
        return p
    
    # Do While loop definition
    @_('DO saveposition block WHILE LPAREN expression RPAREN openjumpslot')
    def dowhileloop(self, p):
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
        self.QM.addOperand((-1, -1))      # To not break the internals of addOperand, add fluff
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
        self.QM.addOperand((-1, -1))      # To not break the internals of addOperand, add fluff
        self.QM.addOperator('P')          # P stands for PRINT
        self.QM.generateQuadruple()       # This makes a print for each parameter (print('a', 'b', ...))        
        return p
    
    # Print a super expression and/or a string
    @_('CTESTRING')
    def writevalues(self, p):
        self.QM.addOperand((p[0], 'string')) # Constants are identified as (constant, type)
        self.QM.addOperand((-1, -1))      # To not break the internals of addOperand, add fluff
        self.QM.addOperator('P')          # P stands for PRINT
        self.QM.generateQuadruple()       # This makes a print for each parameter (print('a', 'b', ...))
        return p

    # Conditional statement    
    @_('IF LPAREN super_exp RPAREN openjumpslot block ELSE filljumps openjumpslot block filljumps')
    def condition(self, p):
        return p

    @_('IF LPAREN super_exp RPAREN openjumpslot block filljumps')
    def condition(self, p):
        return p

    @_('')
    def openjumpslot(self, p):
        # Opening slot for a DO WHILE 
        if p[-7] == 'do' and p[-4] == 'while':   # DO saveposition block WHILE LPAREN expression RPAREN <WE ARE HERE> filljumps
            self.QM.addOperator('GOTOT')
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()


        # Opening slot for an IF
        elif p[-1] == ')' or p[-10] == 'from':    # if (condition) <WE ARE HERE> {statements}
            self.QM.addOperator('GOTOF')
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()
            self.QM.jumps.append(self.QM.QuadrupleNumber)
            
        # Opening slot for an ELSE
        elif p[-2] == 'else':   # if (condition) {statements} ELSE filljumps <WE ARE HERE> {statements}
            self.QM.addOperator('GOTO')
            self.QM.addOperand((-1, -1))
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()
            self.QM.jumps.append(self.QM.QuadrupleNumber)
        

        return p
    
    @_('')
    def saveposition(self, p):
        self.QM.jumps.append(self.QM.QuadrupleNumber + 1)
        return p

    @_('')
    def filljumps(self, p):
        '''
        When filling an ELSE statement, we have to fill the previous jump AHEAD
        of the current quadruple location, since the current location is a GOTO,
        resulting in an infinite loop
        '''
        if p[-1] == 'else':
            quadrupleToFill = self.QM.jumps.pop()
            jumpToPosition = self.QM.QuadrupleNumber + 2       # Jump to position ahead
            self.QM.fillJumps(quadrupleToFill, jumpToPosition) # Fill previous quadruple with position ahead
        

        elif p[-7] == 'while':
            # Generate GOTO quadruple that will return us to before the WHILE's condition
            self.QM.addOperator('GOTO')
            self.QM.addOperand((-1, -1))
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()
            
            # Fill the WHILE's condition (GOTOF) with position AFTER the GOTO we just created
            quadrupleToFill = self.QM.jumps.pop()
            jumpToPosition = self.QM.QuadrupleNumber + 1        # Jump AFTER the GOTO instruction
            self.QM.fillJumps(quadrupleToFill, jumpToPosition)  # Fill previous quadruple with position ahead
            
            # Fill the GOTO quadruple that will return us to before the WHILE's condition
            whileStartPosition = self.QM.jumps.pop()            # This is the position we left after reading the <WHILE> token
            currentQuadruple = self.QM.QuadrupleNumber          # Immediately fill the GOTO we just created
            self.QM.fillJumps(currentQuadruple, whileStartPosition)

        # HACK: Customize increments (instead of only 1 by 1)
        elif p[-12] == 'from':
            # Get jumps in correct order
            loopEnd = self.QM.jumps.pop()    # 4
            loopReturn = self.QM.jumps.pop() # 3

            # Loop increment quadruple
            controlVariable = (self.QM.quadruples[loopReturn-1][1], 'int') # self.QM.quadruples[loopReturn] is the comparison quadruple -> ('<', VControl, VFinal, Temp)
            self.QM.addOperator('++')
            self.QM.operands.append(controlVariable)
            self.QM.addOperand((1, 'int'))
            self.QM.generateQuadruple()

            # Unfilled return quadruple
            self.QM.addOperator('GOTO')
            self.QM.addOperand((-1, -1))
            self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()

            # Fill GOTOF quadruple
            self.QM.fillJumps(loopEnd, self.QM.QuadrupleNumber+1)
            
            # Fill GOTO quadruple
            self.QM.fillJumps(self.QM.QuadrupleNumber, loopReturn)
            

        # Filling a normal IF statement <- GOTOF
        else:
            quadrupleToFill = self.QM.jumps.pop()
            jumpToPosition = self.QM.QuadrupleNumber + 1
            self.QM.fillJumps(quadrupleToFill, jumpToPosition)
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
    
    # FIXME: Add a semicolon at the end
    @_('RETURN super_exp')
    def returnstmt(self, p):
        prohibitedTypes = ['main', 'prog', 'void']
        if self.OFD.dir[self.OFD.context]['type'] in prohibitedTypes:
            raise semanticError(f'❌ RETURN ERROR | Only typed functions may return values') 
        else:
            # Last operand is the result of the super_exp after the RETURN token
            returnResult = self.QM.operands.pop()
            
            # Get the name for the global variable where the return result will be stored
            resultVarName = self.OFD.dir[self.programName]['table'][self.OFD.context]['name']
            
            # Assign the result of the super_exp to the global return variable for the current function
            # self.QM.addOperator('=')
            
            # Use addOperand function to insert operand without messing with constant tables or other parts
            # self.QM.addOperand((resultVarName, 'return'))
            
            # Directly append to operands to avoid filters in addOperand function (they would pass it as a constant)
            # self.QM.operands.append(returnResult)
            
            # Generate assignment quadruple
            # self.QM.generateQuadruple()

            # Generate END FUNCTION quadruple
            # self.QM.addOperator('ENDFUNC')
            # self.QM.addOperand((-1, -1))
            # self.QM.addOperand((-1, -1))
            # self.QM.generateQuadruple()
            
            self.QM.addOperator('RETURN')
            self.QM.addOperand((resultVarName, 'return'))
            self.QM.operands.append(returnResult)
            # self.QM.addOperand((-1, -1))
            # self.QM.addOperand((-1, -1))
            self.QM.generateQuadruple()

        return p
        
    # Statute definition
    @_('assignment', 'condition', 'write', 'read', 'whileloop', 'dowhileloop', 'forloop', 'call', 'returnstmt')
    def statute(self, p):
        return p
    
    ### HELPER RULES ###
    # Changes context BEFORE entering the new block
        # Usually the context changes AFTER the rule is finished, but this doesn't work for variable tables  
    @_('')
    def changecontext(self, p):
        self.MM.resetContextAddresses()
        self.OVT.cleartable()

        if (p[-2] == 'program'):
            self.OFD.changeContext(self.programName)
        
        elif (p[-1]) == 'main':
            # Define function data in a readable way
            functionName   = 'main'
            functionType   = 'main'
            variableTable  = {}
            startQuadruple = self.QM.QuadrupleNumber + 1
            parameterTable = {}
            signature      = ''
            size           = {
                'params':{'int':0, 'float':0, 'bool':0},
                'local' :{'int':0, 'float':0, 'bool':0},
                'temp'  :{'int':0, 'float':0, 'bool':0}
                }
        
            # Pack data ina tuple
            functionData   = (
                functionName, 
                functionType, 
                variableTable, 
                startQuadruple, 
                parameterTable, 
                signature,
                size
            )
            
            # Unpack data and add function to directory
            self.OFD.addfunc(*functionData)
            self.OFD.changeContext(p[-1])
            
            # Fill jump to main
            quadrupleToFill = self.QM.jumps.pop()
            jumpToPosition = self.QM.QuadrupleNumber + 1
            self.QM.fillJumps(quadrupleToFill, jumpToPosition)

        else:
            # If its a typed function it returns a tuple like ('type', 'int')
            if isinstance(p[-2], tuple):
                functionType = p[-2][1]
                
                # Add function as a global variable (to store the value it returns)
                functionResultAddress = self.MM.buildAddress(functionType, 'global')
                self.OFD.dir[self.programName]['table'][p[-1]] = {
                    'name': p[-1],
                    'type': functionType,
                    'scope': self.programName,
                    'address': functionResultAddress
                }
            
            # Otherwise it only returns a 'VOID' string        
            else:
                functionType = p[-2]

            # Define function data in a readable way
            functionName = p[-1]
            variableTable  = {}
            startQuadruple = self.QM.QuadrupleNumber + 1
            parameterTable = {}
            signature      = ''
            size           = {
                'params':{'int':0, 'float':0, 'bool':0},
                'local' :{'int':0, 'float':0, 'bool':0},
                'temp'  :{'int':0, 'float':0, 'bool':0}
                }
            # Pack data ina tuple
            functionData   = (
                functionName, 
                functionType, 
                variableTable, 
                startQuadruple, 
                parameterTable, 
                signature,
                size
            )
            
            # Unpack data and add function to directory
            self.OFD.addfunc(*functionData)
            self.OFD.changeContext(p[-1])
    
    # DOC: Save the program name ASAP to identify repeated variable & function names
    @_('')
    def saveprogramname(self, p):
        # Save program name to check for global variables later
        Pname = p[-1]
        
        # Know how to reference the GLOBAL context from other components
        self.programName     = Pname
        self.OFD.programName = Pname
        self.OVT.programName = Pname
        self.OFD.context     = Pname
        self.MM.programName  = Pname

        # Define function data in a readable way
        functionName   = self.programName
        functionType   = 'prog'
        variableTable  = {}
        startQuadruple = self.QM.QuadrupleNumber + 1
        parameterTable = {}
        signature      = ''
        size           = {
                'params':{'int':0, 'float':0, 'bool':0},
                'local' :{'int':0, 'float':0, 'bool':0},
                'temp'  :{'int':0, 'float':0, 'bool':0}
                }
        
        # Pack data ina tuple
        functionData   = (
            functionName, 
            functionType, 
            variableTable, 
            startQuadruple, 
            parameterTable, 
            signature,
            size
        )
        
        # Unpack data and add function to directory
        self.OFD.addfunc(*functionData)
        
        # Generate GOTO MAIN quadruple
        self.QM.addOperator('GOTO')
        self.QM.addOperand((-1, -1))
        self.QM.addOperand((-1, -1))
        self.QM.generateQuadruple()
        self.QM.jumps.append(self.QM.QuadrupleNumber)

        # Return the ID again so that global declare block can have a name
            # If not returned, the declare block takes p[-1], which would be 
            # whatever we return here (or not)
        return p[-1]

    @_('')
    def empty(self, p):
        pass

    def error(self, p):
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
