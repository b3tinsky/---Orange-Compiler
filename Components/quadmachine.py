from Components.status import semanticError

class OrangeQuadMachine():
    def __init__(self, OFD, SC, MM) -> None:
        self.OFD = OFD              # Orange Function Directory 
        self.SC = SC.cube           # Semantic Cube
        self.MM = MM                # Memory Manager
        self.operators  = [[]]      # [] are added to simulate parenthesis priority
        self.operands    = []       # ('name', 'type')      <- Operand structure
        self.quadruples  = []       # ('+', 'c', 'd', 'T1') <- Quadruple structure
        self.jumps       = []       # Pending jump instructions
        self.TempNumber      = 0    # Number to track temp variables
        self.ParameterNumber = 0    # Number to track parameters
        self.CallSignature   = ''   # Recreated a signature for a function
        self.QuadrupleNumber = 0    # Number to track quadruple numbers (helps with GOTOs)
    
    # HACK: Morph into memory management/tracking
    # Keeps track of temporary variable names
    def generateTempVar(self, resultType):
        address = self.MM.buildAddress(resultType, 'temp')
        # self.TempNumber += 1
        self.OFD.dir[self.OFD.context]['size']['temp'][resultType] += 1
        # return f'T{self.TempNumber}'
        return address

    def generateParameter(self):
        self.ParameterNumber += 1
        return self.ParameterNumber

    def addOperand(self, operand):
        # Constants <- 5 | 12.3 | "name"
            # Passed as tuples (constant, type)
        
        # Filler operands
        if operand == (-1, -1):
            self.operands.append(operand)
        
        # HACK: Convert to a dictionary type switch to make it faster
        # Constants, Functions, Parameters & Returns
        elif isinstance(operand, tuple):
            # Functions
            if operand[1] == 'func':
                self.operands.append(operand)
            
            # Parameters
            elif operand[1] == 'param':
                self.operands.append(operand)
            
            # HACK: Instead of constantly fetching programName from OFD, fetch it once and call it from QM
            # Return
            elif operand[1] == 'return':
                returnAddress = self.OFD.dir[self.OFD.programName]['table'][operand[0]]['address']
                returnType    = self.OFD.dir[self.OFD.programName]['table'][operand[0]]['type']
                self.operands.append( (returnAddress, returnType) )

            # Constants
            else:
                constant     = operand[0]
                constantType = operand[1]
                constantAddress = self.OFD.checkConst(constant, constantType)
                self.operands.append((constantAddress, constantType))

        
        # Variables <- (id, type)
        else:
            
            operandAddress, operandType = self.OFD.checkVar(operand)
            self.operands.append((operandAddress, operandType))
    
    
    def addOperator(self, operator):
        # Append to latest 'fake floor'
            # To manage parenthesis, 'fake floors' are added as lists
            # [[+],[-],[*]] <- a + (c - (b * d))
        self.operators[-1].append(operator)
    

    def generateQuadruple(self):
        self.QuadrupleNumber += 1             # Keep track of quad number
        rightOperand = self.operands.pop()    # ('name', 'type')
        leftOperand = self.operands.pop()     # ('name', 'type')
        operator = self.operators[-1].pop()   # '+' <- [['+']] // Get from latest 'fake floor'

        # Assignment
        if operator == '=':
            try:
                resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]
                self.quadruples.append( (operator, rightOperand[0], -1, leftOperand[0]) ) 
                # self.operands.append( (leftOperand[0], resultType) )

            except:
                raise semanticError(f'❌ Type mismatch | Value for <{leftOperand[0]}> should be of type <{leftOperand[1]}> and instead got <{rightOperand[0]}> with type <{rightOperand[1]}>')
            
            return
        
        # Print
        elif operator == 'P':
            # TODO: Add a custom error message
            # TODO: Add tests about printing weird stuff that shouldn't be allowed
            # Prints the leftOperand because when printing expressions, the operand is added before the blank ('')
            # so constant strings are added the same way to keep consistency
            self.quadruples.append( (operator, -1, -1, leftOperand[0]) ) 
            return

        # Input
        elif operator == 'R':
            # TODO: Add a custom error message
            # TODO: Add tests about reading weird stuff that shouldn't be allowed
            # Prints the leftOperand because when printing expressions, the operand is added before the blank ('')
            # so constant strings are added the same way to keep consistency
            self.quadruples.append( (operator, -1, -1, leftOperand[0]) ) 
            return
        
        # Conditional
            # IF
        elif operator == 'GOTOF':
            # Validates that contiion results in a boolean <- if (a + b > c * d)
            if leftOperand[1] == 'bool':
                # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
                self.quadruples.append( (operator, leftOperand[0], -1, '?') ) 
            
            # If condition does not result in a boolean, a special mismatch error is raised
            else:
                raise semanticError(f'❌ Type mismatch | Condition must result in a boolean value')
            
            return
        
            # DO WHILE
        elif operator == 'GOTOT':
            # Validates that contiion results in a boolean <- if (a + b > c * d)
            if leftOperand[1] == 'bool':
                jumpToPosition = self.jumps.pop()
                # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
                self.quadruples.append( (operator, leftOperand[0], -1, jumpToPosition) ) 
            
            # If condition does not result in a boolean, a special mismatch error is raised
            else:
                raise semanticError('❌ Type mismatch. Condition must result in a boolean value.')
            
            return

            # ELSE
        elif operator == 'GOTO':
            # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
            self.quadruples.append( (operator, -1, -1, '?') ) 
            return
        
        # ENDFUNC
        elif operator == 'ENDFUNC':
            # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
            self.quadruples.append( (operator, -1, -1, -1) ) 
            return

        # ERA
        elif operator == 'ERA':
            # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
            self.quadruples.append( (operator, -1, -1, leftOperand[0]) ) 
            return

        # ERA
        elif operator == 'PARAM':
            # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
            self.quadruples.append( (operator, leftOperand[0], -1, rightOperand[0]) ) 
            return

        # GOSUB
        elif operator == 'GOSUB':
            # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
            self.quadruples.append( (operator, -1, -1, leftOperand[0]) ) 
            return

        elif operator == '++':
            self.quadruples.append( (operator, leftOperand[0], rightOperand[0], leftOperand[0]) ) 

        # SUM, MULT, DIV, SUB, GT, GTE, LT, LTE, EQ, NEQ
        else:
        # If there is a type mismatch:
            # A key won't be found, causing an error
            try:
                resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]

                tmpVar = self.generateTempVar(resultType)

                # Add the quadruple to quadruple list
                self.quadruples.append( (operator, leftOperand[0], rightOperand[0], tmpVar) ) 

                # Return the temporary variable to operands
                self.operands.append( (tmpVar, resultType) )
            except:
                arithmetic = ['+', '-', '*', '/']
                relational = ['>', '>=', '<', '<=', '==', '!=']
                
                if operator in arithmetic:
                    raise semanticError(f'❌ Type mismatch | Value for <{leftOperand[0]}> should be of type {leftOperand[1]}> and instead got <{rightOperand[0]}> with type <{rightOperand[1]}>')
                
                elif operator in relational:
                    raise semanticError(f'❌ Type mismatch | Relations must be numeric and instead tried to compare <{leftOperand[0]}> of type <{leftOperand[1]}> with <{rightOperand[0]}> of type <{rightOperand[1]}>')
    
    
    def fillJumps(self, quadrupleToFill, jumpToPosition):
        # quadrupleToFill <- Quadruple number that doesn't know where to jump
            # -1 to use index in list

        # Copy quadruple info
            # Since quadruples are stored as tuples, we can't directly mutate them
        operator, leftOperand, rightOperand, _ = self.quadruples[quadrupleToFill - 1]

        # Replace with new quadruple
            # Quadruples are stored in a list (lists are mutable, but tuples themselves are not)
        self.quadruples[quadrupleToFill - 1] = (operator, leftOperand, rightOperand, jumpToPosition)
    
    # Prints quadruples for an easier review
    def printQuads(self):
        counter = 1
        for quad in self.quadruples:
            print(f'{str(counter):2s} | {str(quad[0]):10s} {str(quad[1]):10s} {str(quad[2]):10s} {str(quad[3]):10s} |')
            counter+=1
        
        # For testing purposes
        # print()
        # print(self.quadruples)