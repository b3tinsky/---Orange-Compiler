from Components.status import semanticError
import sys
import pickle

class VirtualMachine():
    def __init__(self):
        self.quadruples        = None
        self.functiondirectory = None
        self.constants         = None
        self.memory            = []
        self.IP                = 1  # Instruction Pointer
        self.BC                = [] # Bread Crumb (Save position when entering functions)
        self.instructionQty    = 0
        self.programName       = ''
        self.instructionSwitch = {
            '='       : self.assignmentOperator,
            '+'       : self.plusOperator,
            '-'       : self.minusOperator,
            '*'       : self.multOperator,
            '/'       : self.divOperator,
            '>'       : self.gtOperator,
            '>='      : self.gteOperator,
            '<'       : self.ltOperator,
            '<='      : self.lteOperator,
            '=='      : self.eqOperator,
            '!='      : self.neqOperator,
            'P'       : self.printOperator,
            'R'       : self.readOperator,
            'ERA'     : self.eraOperator,
            'VERIFY'  : self.verifyOperator,
            'ENDFUNC' : self.endfuncOperator,
            'RETURN'  : self.returnOperator,
            'GOSUB'   : self.gosubOperator,
            'PARAM'   : self.paramOperator,
            'GOTO'    : self.gotoOperator,
            'GOTOF'   : self.gotofOperator,
            'GOTOT'   : self.gototOperator,
            '++'      : self.incrementOperator,
        }

    # HACK: ARITHMETIC
    # Quadruple example -> ('=', 40000, -1, 20002)
    def assignmentOperator(self, QUAD):
        whatToAssign = self.fetchFromAddress(QUAD[1])
        self.setInAddress(whatToAssign, QUAD[3])
        
    # Quadruple example -> ('+', 20002, 20000, 30000)
    def plusOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue + rightValue, QUAD[3])

    # Quadruple example -> ('-', 20002, 20000, 30000)
    def minusOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue - rightValue, QUAD[3])
    
    # Quadruple example -> ('*', 20002, 20000, 30000)
    def multOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])

        self.setInAddress(leftValue * rightValue, QUAD[3])
        
    # Quadruple example -> ('/', 20002, 20000, 30000)
    def divOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue / rightValue, QUAD[3])
    
    # HACK: COMPARE
    # Quadruple example -> ('>', 30000, 30001, 38000)
    def gtOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue > rightValue, QUAD[3])
    
    # Quadruple example -> ('>=', 30000, 30001, 38000)
    def gteOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue >= rightValue, QUAD[3])
    
    # Quadruple example -> ('<', 30000, 30001, 38000)
    def ltOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue < rightValue, QUAD[3])
    
    # Quadruple example -> ('<=', 30000, 30001, 38000)
    def lteOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue <= rightValue, QUAD[3])
    
    # Quadruple example -> ('==', 30000, 30001, 38000)
    def eqOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue == rightValue, QUAD[3])
    
    # Quadruple example -> ('!=', 30000, 30001, 38000)
    def neqOperator(self, QUAD):
        leftValue = self.fetchFromAddress(QUAD[1])
        rightValue = self.fetchFromAddress(QUAD[2])
        self.setInAddress(leftValue != rightValue, QUAD[3])

    # HACK: AUX
    # Quadruple example -> ('P', -1, -1, 47500)
    def printOperator(self, QUAD):
        # Replace literal whitespace characters with real ones 
        whitespace = {r'\n':'\n', r'\t':'\t', r'\r':'\r'}
        
        # Fetch value to print
        whatToPrint = str(self.fetchFromAddress(QUAD[3]))
        
        # Map
        for key in whitespace.keys():
            whatToPrint = whatToPrint.replace(key, whitespace[key])

        # Print operand
        print(whatToPrint, end='')

    # Quadruple example -> ('R', -1, -1, 10000)
    def readOperator(self, QUAD):
        address = QUAD[3]
        
        if 10000 <= address < 14000 or 20000 <= address < 24000:
            inputValue = int(input())
        
        elif 14000 <= address < 18000 or 24000 <= address < 28000:
            inputValue = float(input())
        
        elif 18000 <= address < 20000 or 28000 <= address < 30000:
            inputValue = bool(input())
            
        self.setInAddress(inputValue, address)

    # Quadruple example -> ('ERA', -1, -1, 'sum')
    def eraOperator(self, QUAD):
        functionName = QUAD[3]
        self.createMemory(functionName)

    # Quadruple example -> ('PARAM', 30010, -1, 2)
    def paramOperator(self, QUAD):
        # Value to initialize parameter
        paramValue = self.fetchFromAddress(QUAD[1])
       
        # Must be turned to list to access by index
        currentMemoryBlock = list(self.memory[-1])

        # Params are added as first local variables in new memory block
        paramAddress = currentMemoryBlock[QUAD[3]-1]

        # Initialize parameter
        self.setInAddress(paramValue, paramAddress)
    
    # Quadruple example -> ('ENDFUNC', -1, -1, -1)
    def endfuncOperator(self, QUAD):
        # Go back to where the function was called
        self.IP = self.BC.pop()

        # Delete function's memory block
        self.memory.pop()

    # Quadruple example -> ('RETURN', 20000, -1, 10003)
    def returnOperator(self, QUAD):
        # Get value to store
        returnValue = self.fetchFromAddress(QUAD[1])
        
        # Store value in global variable for function returns
        self.setInAddress(returnValue, QUAD[3])
        
        # Changes instruction pointer and removes last memory block
        self.endfuncOperator(QUAD)

    
    # Quadruple example -> ('GOSUB', -1, -1, 'sum')
    def gosubOperator(self, QUAD):
        # Function name
        func = QUAD[3]
        
        # Save current position
        self.BC.append(self.IP)

        # Go to function's quadruple
        self.IP = self.functiondirectory[func]['quadruple'] - 1
    
    # Quadruple example -> ('VERIFY', 30002, '-2', '4')
    def verifyOperator(self, QUAD):
        value = self.fetchFromAddress(QUAD[1])
        lowerLimit = int(QUAD[2])
        upperLimit = int(QUAD[3])

        if not (lowerLimit <= value <= upperLimit):
            raise semanticError(f'🚫 Out Of Bounds | Index {value} must be between limits [{lowerLimit} : {upperLimit}]')

    # HACK: JUMPS
    # ('GOTO', -1, -1, 2)
    def gotoOperator(self, QUAD):
        # Change the instruction pointer
        self.IP = QUAD[3] - 1
    
    # ('GOTOF', 38000, -1, 12)
    def gotofOperator(self, QUAD):
        if not self.fetchFromAddress(QUAD[1]):
            # Change the instruction pointer
            self.IP = QUAD[3] - 1

    # ('GOTOT', 38000, -1, 12)
    def gototOperator(self, QUAD):
        if self.fetchFromAddress(QUAD[1]):
            # Change the instruction pointer
            self.IP = QUAD[3] - 1
    
    # ('++', 10008, 40002, 10008)
    def incrementOperator(self, QUAD):
        address = QUAD[3]
        controlVariable = self.fetchFromAddress(QUAD[3])
        incrementAmount = self.fetchFromAddress(QUAD[2])
        self.setInAddress(controlVariable + incrementAmount, address)

    def otherOperator(self, QUAD):
        pass

    def run(self):
        # Bring back compiled data
        self.uploadDump()        
        
        # Execute intermediate code
        while (self.IP <= self.instructionQty):
            currentInstruction = self.IP - 1
            
            # Execute function from instruction switch
            self.instructionSwitch.get(self.quadruples[currentInstruction][0], self.otherOperator)(self.quadruples[currentInstruction])
            
            # Move Instruction Pointer
            self.IP += 1

        print('🌍 AFTER: ', self.memory)

    def createMemory(self, function):
        # Memory block to add to the memory stack
        memoryBlock = {}
        
        # Variable table from the function directory
        table = self.functiondirectory[function]['table']

        # Parameter table from the function directory
        parameters = self.functiondirectory[function]['params']
        
        # Size requirements for function
        temps = self.functiondirectory[function]['size']['temp']
        
        # Size requirements for pointers in a function
        pointers = self.functiondirectory[function]['size']['pointers']

        # Open space for local variables
        if table:
            for variable in table:
                memoryBlock[table[variable]['address']] = None
        
        # Open space for parameters (as local variables)
        if parameters:
            for variable in parameters:
                memoryBlock[parameters[variable]['address']] = None
        
        # Open space for pointers (as local variables)
        if pointers:
            for pointer in pointers:
                memoryBlock[pointer] = None

        # Open space for temporary variables
        intTempAddress = 30000
        for intTemp in range(temps['int']):
            memoryBlock[intTempAddress] = None
            intTempAddress += 1
        
        floatTempAddress = 34000
        for floatTemp in range(temps['float']):
            memoryBlock[floatTempAddress] = None
            floatTempAddress += 1
        
        boolTempAddress = 38000
        for boolTemp in range(temps['bool']):
            memoryBlock[boolTempAddress] = None
            boolTempAddress += 1

        self.memory.append(memoryBlock)

    def uploadDump(self):
        try:
            with open('ovejota.pickle', 'rb') as obj:
                DUMP = pickle.load(obj)
            self.quadruples        = DUMP['quadruples']
            self.functiondirectory = DUMP['functiondirectory']
            # Import directly the addresses and values
            self.constants         = dict(DUMP['constantstable']['int'] | DUMP['constantstable']['float'] | DUMP['constantstable']['bool'] | DUMP['constantstable']['string'])
            
            # Invert dictionary
                # Prev  -> {1: 40000, "Hello": 47500} The value is the key
                # After -> {40000: 1, 47500: "Hello"} The address is the key
            self.constants = {val: key for key, val in self.constants.items()}
            
            self.programName       = DUMP['programname']
            self.instructionQty    = len(self.quadruples)
            self.createMemory(self.programName)
            self.createMemory('main')
        
        except:
            raise semanticError('❌ Object file not found')

    def fetchFromAddress(self, address):
        # Address
        if isinstance(address, str):
            address = int(address)

            # Just make it positive and return the address (no actual fetching)
            if address < 50000:
                return int(address)
                
        
        # Global variables
        if 10000 <= address < 20000:
            return self.memory[0][address]
        
        # Local variables
        elif 20000 <= address < 30000:
            if address in self.memory[-1] and self.memory[-1][address] != None:
                return self.memory[-1][address]
            
            elif address in self.memory[-2] and self.memory[-2][address] != None:
                return self.memory[-2][address]
            
            else:
                return self.memory[-1][address]

        # Temp variables
        elif 30000 <= address < 40000:
            return self.memory[-1][address]
            
        # Constants
        elif 40000 <= address < 50000:
            return self.constants[address]

        # Pointers
        elif 50000 <= address < 60000:
            pointer = self.memory[-1][address]
            pointerContent = self.fetchFromAddress(pointer)
            return pointerContent

        
    def setInAddress(self, value, address):
        # Address
        if isinstance(address, str):
            # Just make it positive and return the address (no actual fetching)
            pointer = self.memory[-1][int(address)]
            address = pointer
            if 10000 <= address < 20000:
                self.memory[0][address] = value
            elif 20000 <= address < 60000:
                self.memory[-1][address] = value


        elif 10000 <= address < 20000:
            self.memory[0][address] = value
        
        # elif 20000 <= address < 40000:
        #     self.memory[-1][address] = value
        
        elif 20000 <= address < 60000:
            self.memory[-1][address] = value
        
        # elif 50000 <= address < 60000:
        #     self.memory[-1][address] = value
            # pointer = self.memory[-1][address]
            # if 10000 <= address < 20000:
            #     self.memory[0][pointer] = value
            # elif 20000 <= address < 40000:
            #     self.memory[-1][pointer] = value
        
    def printQuads(self):
        counter = 1
        for quad in self.quadruples:
            print(f'{str(counter):2s} | {str(quad[0]):10s} {str(quad[1]):10s} {str(quad[2]):10s} {str(quad[3]):10s} |')
            counter+=1

    # https://www.upgrad.com/blog/how-to-implement-switch-case-functions-in-python/