import yaml
from Components.status import semanticError

class OrangeFuncDir():

    # DOC: Specify what each variable is/ what its for/ etc.
    def __init__(self, status):
        self.StatusChecker = status
        self.dir = {}
        
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
        # Look for var in the current scope
        if var_id in self.dir[self.context]['table']:
            # TODO: Return memory address
            varName = self.dir[self.context]['table'][var_id]['name']
            varType = self.dir[self.context]['table'][var_id]['type']
            return varName, varType
        
        elif var_id in self.dir[self.context]['params']:
            # TODO: Return memory address
            varName = self.dir[self.context]['params'][var_id]['name']
            varType = self.dir[self.context]['params'][var_id]['type']
            return varName, varType
        
        # Look for var in the global scope
        elif var_id in self.dir[self.programName]['table']:
            # TODO: Return memory address
            varName = self.dir[self.programName]['table'][var_id]['name']
            varType = self.dir[self.programName]['table'][var_id]['type']
            return varName, varType
        
        # Raise semantic error for trying to use undeclared variables
        else:
            raise semanticError(f'❌ Undeclared variable < {var_id} > in scope < {self.context} >')


    def addParam(self, pName, pType):
        # Add parameter to parameters dictionary
        self.dir[self.context]['params'][pName] = {'name': pName, 'type': pType, 'scope': self.context}

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
        # self.dir[self.context]['signature'].append(pType)

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
        print(yaml.dump(self.dir, default_flow_style=False))
        
        # PRINT DICT - To copy and paste for tests
        # print(self.dir)
