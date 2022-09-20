import yaml
from Components.status import semanticError

class OrangeFuncDir():

    def __init__(self, status):
        self.StatusChecker = status
        self.dir = {}
        
        # DOC: Start with a global context. As functions and main() are declared, the context changes
        self.context = 'global'


    def checkfunc(self, func):
        # Function already exists
        if func in self.dir:
            return True
        
        # Function doesn't exist
        else:
            return False

    def addfunc(self, id, type, table):
        if self.checkfunc(id):
            # self.StatusChecker.semanticError()
            raise semanticError(f'🚫 Function < {id} > already exists')

        else:
            print(f'✅ Function < {id} > successfully added')
            self.dir[id] = {'name': id, 'type': type, 'table': table}


    def changeContext(self, currentContext):
        self.context = currentContext

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
        print(self.dir)
