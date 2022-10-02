from Components.status import semanticError

class OrangeQuadMachine():
    def __init__(self, OFD, SC) -> None:
        self.OFD = OFD              # Orange Function Directory 
        self.SC = SC.cube           # Semantic Cube
        self.operators  = [[]]      # [] are added to simulate parenthesis priority
        self.operands    = []       # ('name', 'type')      <- Operand structure
        self.quadruples  = []       # ('+', 'c', 'd', 'T1') <- Quadruple structure
        self.jumps       = []       # Pending jump instructions
        self.TempNumber      = 0    # Number to track temp variables
        self.QuadrupleNumber = 0    # Number to track quadruple numbers (helps with GOTOs)
    
    # HACK: Morph into memory management/tracking
    # Keeps track of temporary variable names
    def generateTempVar(self):
        self.TempNumber += 1
        return f'T{self.TempNumber}'

    def addOperand(self, operand):
        # Constants <- 5 | 12.3 | "name"
            # Passed as tuples (constant, type)
        if isinstance(operand, tuple):
            operandName = operand[0]
            operandType = operand[1]
            self.operands.append((operandName, operandType))
            

        # Variables <- (id, type)
        else:
            operandName, operandType = self.OFD.checkVar(operand)
            self.operands.append((operandName, operandType))
    
    
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

        # Try catch because if the semantic cube doesn't have [type][operator][type]
        # the error should be catched and a semantic error should be raised
        try:
            mismatchErrorMessage = f'❌ Type mismatch. Condition must result in a boolean.'
            # Assignment
            if operator == '=':
                self.quadruples.append( (operator, rightOperand[0], '', leftOperand[0]) ) 
                return
            
            # Print
            elif operator == 'P':
                # Prints the leftOperand because when printing expressions, the operand is added before the blank ('')
                # so constant strings are added the same way to keep consistency
                self.quadruples.append( (operator, '', '', leftOperand[0]) ) 
                return

            # Input
            elif operator == 'R':
                # Prints the leftOperand because when printing expressions, the operand is added before the blank ('')
                # so constant strings are added the same way to keep consistency
                self.quadruples.append( (operator, '', '', leftOperand[0]) ) 
                return
            
            # Conditional
            # IF
            elif operator == 'GOTOF':
                # Validates that contiion results in a boolean <- if (a + b > c * d)
                if leftOperand[1] == 'bool':
                    # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
                    self.quadruples.append( (operator, leftOperand[0], '', '?') ) 
                    
                    # Store quadruple number to later fill
                    # self.jumps.append(self.QuadrupleNumber)
                
                # If condition does not result in a boolean, a special mismatch error is raised
                else:
                    mismatchErrorMessage = '❌ Type mismatch. Condition must result in a boolean value.'
                
                return

            # ELSE
            elif operator == 'GOTO':
                # Adds quadruple, but at this point it doesn't know where to jump in case condition is not met
                self.quadruples.append( (operator, '', '', '?') ) 
                
                # Store quadruple number to later fill
                # self.jumps.append(self.QuadrupleNumber)
                
                
                return

            
            # If there is a type mismatch:
                # A key won't be found, causing an error
            resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]
        except:
            raise semanticError(mismatchErrorMessage)

        tmpVar = self.generateTempVar()




        # Add the quadruple to quadruple list
        self.quadruples.append( (operator, leftOperand[0], rightOperand[0], tmpVar) ) 

        # Return the temporary variable to operands
        # TODO: Change temp var names (strings) to memory spaces
        self.operands.append( (tmpVar, resultType) )
    
    
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
            print(f'{str(counter):2s} | {quad[0]:10s} {quad[1]:10s} {quad[2]:10s} {str(quad[3]):10s} |')
            counter+=1