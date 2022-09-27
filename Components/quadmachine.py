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

        
        # If there is a type mismatch:
            # A key won't be found, causing an error
        resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]
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