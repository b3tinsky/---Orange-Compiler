import yaml
from Components.status import semanticError

class OrangeVarTable():
    def __init__(self, status, memory):
        self.StatusChecker = status
        self.MemoryManager = memory
        self.programName = '' # Global scope
        self.table = {}
        self.varType = ''

    def checkvar(self, var, currentFuncDir):
        
        # Variable already exists in current context
        if var in self.table:
            return True
        
        # Variable already exists in global scope
        # elif currentFuncDir:
        #     if var in currentFuncDir['table']:
        #         print(f'🚫 Variable < {var} > already exists in global context')
        #         return True
            
        #     else:
        #         return False

        # Variable doesn't exist in current context
        else:
            return False
        
        

    def addvar(self, id, type, scope, currentFuncDir):
        if self.checkvar(id, currentFuncDir):
            raise semanticError(f'🚫 Variable < {id} > already exists in current context')

        else:
            # print(f'✅ Variable < {id} > successfully added')
            # TODO: Generate virtual address depending on type & scope
            address = self.MemoryManager.buildAddress(type, 'global' if scope == self.programName else 'local')
            self.table[id] = {
                'name': id, 
                'type': type, 
                'scope': scope,
                'address': address
                }

    '''
    Tokenstream is the complete token stream provided by the rules:
        type decvar SEMICOLON
        type decvar SEMICOLON decvar_line
    
    This means tokenstream[0] represents the type token stream:
        ('type', 'float')
    
    And tokenstream[1] represents all the IDs declared in that stream:
        ('decvar', ('var', 'x'), ',', ('decvar', ('var', 'y'), ',', ('decvar', ('var', 'z'))))
    '''
    def addvartokenstream(self, tokenstream, scope, currentFuncDir):
        # Variable type
        varType = tokenstream[0][1]

        # Variable names
        flattenedTokenStream = self.flattentokenstream(tokenstream[1])

        # Add each variable name with the established type for the line and current scope/context
        for i in flattenedTokenStream:
            self.addvar(i, varType, scope, currentFuncDir)
            

    '''
    Flattens the token stream by returning each individual value instead of nested tuples
        From:
            ('decvar', ('var', 'x'), ',', ('decvar', ('var', 'y'), ',', ('decvar', ('var', 'z'))))
        To:
            'decvar', 'var', 'x', ',', 'decvar', 'var', 'y', ',', 'decvar', 'var', 'z'
        
        Also, removes reserved tokens like commas, 'var', and 'decvar' while flattening
    '''
    def flattentokenstream(self, d):
        reservedTokens = [',', 'var', 'decvar']
        for i in d:
            if i not in reservedTokens:
                yield from [i] if not isinstance(i, tuple) else self.flattentokenstream(i)
        



    def cleartable(self):
        self.table = {}

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
        print(yaml.dump(self.table, default_flow_style=False))
        
        # PRINT DICT - To copy and paste for tests
        # print(self.table)
