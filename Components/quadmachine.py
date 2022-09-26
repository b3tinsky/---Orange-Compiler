class OrangeQuadMachine():
    def __init__(self, OFD, SC) -> None:
        self.OFD = OFD              # Orange Function Directory 
        self.SC = SC.cube                # Semantic Cube
        self.operands  = []
        self.operators = []
        self.quadruples = []
        self.TempNumber = 0         # Number to track temp variables

    def generateTempVar(self):
        self.TempNumber += 1
        return f'T{self.TempNumber}'

    def addOperand(self, operand):
        operandName, operandType = self.OFD.checkVar(operand)
        self.operands.append((operandName, operandType))
    
    def addOperator(self, operator):
        self.operators.append(operator)
    
    def generateQuadruple(self):
        # Since list acts as a stack, right operand must be popped first
        rightOperand = self.operands.pop() # ('name', 'type')
        leftOperand = self.operands.pop()  # ('name', 'type')
        operator = self.operators.pop()    # '+'
        
        # If there is a type mismatch:
            # A key won't be found, causing an error
        resultType = self.SC[leftOperand[1]][operator][rightOperand[1]]
        tmpVar = self.generateTempVar()

        # Add the quadruple to quadruple list
        self.quadruples.append( (operator, leftOperand[0], rightOperand[0], tmpVar) ) 

        # Return the temporary variable to operands
        # TODO: Change temp var names (strings) to memory spaces
        self.operands.append( (tmpVar, resultType) )
    