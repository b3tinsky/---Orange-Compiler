import yaml
from Components.status import semanticError

class OrangeFuncDir():

    # DOC: Specify what each variable is/ what its for/ etc.
    def __init__(self, status, memory):
        self.StatusChecker = status
        self.MemoryManager = memory
        self.dir = {}
        self.constants = {
            'int'   : {},
            'float' : {},
            'bool'  : {},
            'string': {}
        }

        # DOC: Start with a global context. As functions and main() are declared, the context changes
        self.context = ''
        
        # Helps looking for global variables
        self.programName = ''

    # DOC: Use PEP standard for this docstring
    '''
    Checks if the function name is already taken or not
    '''
    def checkfunc(self, func):
        # Function already exists
        if func in self.dir:
            return True
        
        # Function doesn't exist
        else:
            return False

    # DOC: Use PEP standard for this docstring
    '''
    Adds function to the function directory
    '''
    def addfunc(self, id, type, table, quadrupleNumber, params, signature, size):
        if self.checkfunc(id):
            raise semanticError(f'❌ Function < {id} > already exists')

        else:
            self.dir[id] = {
                'name': id, 
                'type': type, 
                'table': table, 
                'quadruple': quadrupleNumber,
                'params': params,
                'signature': signature,
                'size': size
                }

    # DOC: Use PEP standard for this docstring
    '''
    Changes current context when entering a new function block/scope.
    '''
    def changeContext(self, currentContext):
        self.context = currentContext
    
    # DOC: Use PEP standard for this docstring
    '''
    Checks if a variable exists. This prevents the usage of undeclared variables.
    '''
    def checkVar(self, var_id):
        # Look for var in the current scope variables
        if var_id in self.dir[self.context]['table']:
            # varName = self.dir[self.context]['table'][var_id]['name']
            varAddress = self.dir[self.context]['table'][var_id]['address']
            varType    = self.dir[self.context]['table'][var_id]['type']
            return varAddress, varType
        
        # Look for var in the current scope parameters
        elif var_id in self.dir[self.context]['params']:
            # varName = self.dir[self.context]['params'][var_id]['name']
            varAddress = self.dir[self.context]['params'][var_id]['address']
            varType = self.dir[self.context]['params'][var_id]['type']
            return varAddress, varType
        
        # Look for var in the global scope
        elif var_id in self.dir[self.programName]['table']:
            # varName = self.dir[self.programName]['table'][var_id]['name']
            varAddress = self.dir[self.programName]['table'][var_id]['address']
            varType = self.dir[self.programName]['table'][var_id]['type']
            return varAddress, varType
        
        # Raise semantic error for trying to use undeclared variables
        else:
            raise semanticError(f'❌ Undeclared variable < {var_id} > in scope < {self.context} >')

    def getVar(self, var_id):
        # Look for var in the current scope variables
        if var_id in self.dir[self.context]['table']:
            return self.dir[self.context]['table'][var_id]
        
        # Look for var in the current scope parameters
        elif var_id in self.dir[self.context]['params']:
            return self.dir[self.context]['params'][var_id]
        
        # Look for var in the global scope
        elif var_id in self.dir[self.programName]['table']:
            return self.dir[self.programName]['table'][var_id]
        
        # Raise semantic error for trying to use undeclared variables
        else:
            raise semanticError(f'❌ Undeclared variable < {var_id} > in scope < {self.context} >')

    def addParam(self, pName, pType):
        address = self.MemoryManager.buildAddress(pType, 'local')
        # Add parameter to parameters dictionary
        self.dir[self.context]['params'][pName] = {'name': pName, 'type': pType, 'scope': self.context, 'address': address}

        # Add parameter type to signature
        if pType == 'int':
            self.dir[self.context]['signature'] += 'i'
            self.dir[self.context]['size']['params']['int'] += 1
        elif pType == 'float':
            self.dir[self.context]['signature'] += 'f'
            self.dir[self.context]['size']['params']['float'] += 1
        elif pType == 'bool':
            self.dir[self.context]['signature'] += 'b'
            self.dir[self.context]['size']['params']['bool'] += 1

    def addConst(self, constant, constantType):
        # Generate address for the constant
        address = self.MemoryManager.buildAddress(constantType, 'const')
        
        # Add constant and its address to the constant table
        self.constants[constantType][constant] = address
        
        return address

    def checkConst(self, constant, constantType):
        # Look for constant in the constant table
        if constant in self.constants[constantType]:
            constantAddress = self.constants[constantType][constant]
            return constantAddress
        
        # If constant is not found, make an address and add it
        else:
            # Returns address
            return self.addConst(constant, constantType)

    '''
    Prettifies printing the data for the variable table by turning it to YAML
    # Normal print #
    {'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}

    # Pretty print (by turning it to YAML)
    a: 2
    b:
        x: 3
        y:
            t1: 4
            t2: 5
    '''
    def printdata(self):
        # PRINT YAML - Human readable
        print(yaml.dump(self.constants, default_flow_style=False))
        print(yaml.dump(self.dir, default_flow_style=False))
        
        # PRINT DICT - To copy and paste for tests
        # print(self.dir)
