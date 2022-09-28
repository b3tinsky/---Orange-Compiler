from Components.status import semanticError

class OrangeQuadMachine():
    def __init__(self, OFD, SC) -> None:
        self.OFD = OFD              # Orange Function Directory 
        self.SC = SC.cube           # Semantic Cube
        self.operands  = []
        self.operators = [[]]       # [] are added to simulate parenthesis priority
        self.quadruples = []        # ('+', 'c', 'd', 'T1') <- Quadruple structure
        self.TempNumber = 0         # Number to track temp variables
    
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
        rightOperand = self.operands.pop()    # ('name', 'type')
        leftOperand = self.operands.pop()     # ('name', 'type')
        operator = self.operators[-1].pop()   # '+' <- [['+']] // Get from latest 'fake floor'

        # Try catch because if the semantic cube doesn't have [type][operator][type]
        # the error should be catched and a semantic error should be raised
        try:
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

            
            # If there is a type mismatch:
                # A key won't be found, causing an error
            resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]
        except:
            raise semanticError(f'❌ Type mismatch {leftOperand} with {rightOperand}')

        tmpVar = self.generateTempVar()




        # Add the quadruple to quadruple list
        self.quadruples.append( (operator, leftOperand[0], rightOperand[0], tmpVar) ) 

        # Return the temporary variable to operands
        # TODO: Change temp var names (strings) to memory spaces
        self.operands.append( (tmpVar, resultType) )
    
    # Prints quadruples for an easier review
    def printQuads(self):
        counter = 1
        for quad in self.quadruples:
            print(f'{counter}\t|  {quad[0]}\t  {quad[1]}\t{quad[2]}\t{quad[3]}\t|')
            counter+=1