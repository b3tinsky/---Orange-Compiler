from Components.status import semanticError

class MemoryManager():
    
    def __init__(self):
        self.programName = '' # Global scope
    
        self.addressBook = {
            'global': {
                'base'  : 10000,    # Base Address
                'int'   : 0,        # Range for ints    10,000 - 13,999
                'float' : 4000,     # Range for floats  14,000 - 17,999
                'bool'  : 8000      # Range for bools   18,000 - 19,999
            },
            'local': {
                'base'  : 20000,    # Base Address
                'int'   : 0,        # Range for ints    20,000 - 23,999
                'float' : 4000,     # Range for floats  24,000 - 27,999
                'bool'  : 8000      # Range for bools   28,000 - 29,999
            },
            'temp': {
                'base'  : 30000,    # Base Address
                'int'   : 0,        # Range for ints    30,000 - 33,999
                'float' : 4000,     # Range for floats  34,000 - 37,999
                'bool'  : 8000      # Range for bools   38,000 - 39,999
            },
            'const': {
                'base'   : 40000,   # Base Address
                'int'    : 0,       # Range for ints    40,000 - 42,499
                'float'  : 2500,    # Range for floats  42,500 - 44,999
                'bool'   : 5000,    # Range for bools   45,000 - 47,499
                'string' : 7500     # Range for strings 47,500 - 49,999                
            }     
        }

        # memory = {} # Address : content
        self.GM = {}       # Global    Memory
        self.LM = {}       # Local     Memory
        self.TM = {}       # Temporary Memory
        self.CM = {}       # Constant  Memory

    # HACK: Change memory limits to dynamic instead of static
    # When building the memory address, checks if the proposed memory address is out of bounds
    def checkMemoryLimits(self, type, scope):
        # Returns a True or False based on memory limits (by scope and type) 
        return  {
            ('global', 'int'   ) : lambda: 10000 <= self.addressBook['global']['base'] + self.addressBook['global']['int']   < 14000,
            ('global', 'float' ) : lambda: 14000 <= self.addressBook['global']['base'] + self.addressBook['global']['float'] < 18000,
            ('global', 'bool'  ) : lambda: 18000 <= self.addressBook['global']['base'] + self.addressBook['global']['bool']  < 20000,
            ('local' , 'int'   ) : lambda: 20000 <= self.addressBook['local']['base']  + self.addressBook['local']['int']    < 24000,
            ('local' , 'float' ) : lambda: 24000 <= self.addressBook['local']['base']  + self.addressBook['local']['float']  < 28000,
            ('local' , 'bool'  ) : lambda: 28000 <= self.addressBook['local']['base']  + self.addressBook['local']['bool']   < 30000,
            ('temp'  , 'int'   ) : lambda: 30000 <= self.addressBook['temp']['base']   + self.addressBook['temp']['int']     < 34000,
            ('temp'  , 'float' ) : lambda: 34000 <= self.addressBook['temp']['base']   + self.addressBook['temp']['float']   < 38000,
            ('temp'  , 'bool'  ) : lambda: 38000 <= self.addressBook['temp']['base']   + self.addressBook['temp']['bool']    < 40000,
            ('const' , 'int'   ) : lambda: 40000 <= self.addressBook['const']['base']  + self.addressBook['const']['int']    < 42500,
            ('const' , 'float' ) : lambda: 42500 <= self.addressBook['const']['base']  + self.addressBook['const']['float']  < 45000,
            ('const' , 'bool'  ) : lambda: 45000 <= self.addressBook['const']['base']  + self.addressBook['const']['bool']   < 47500,
            ('const' , 'string') : lambda: 47500 <= self.addressBook['const']['base']  + self.addressBook['const']['string'] < 50000
        }.get((scope, type), lambda: None)

    def buildAddress(self, type, scope):
        if self.checkMemoryLimits(type, scope)():
            # Build address
            address = self.addressBook[scope]['base'] + self.addressBook[scope][type]

            # Update typed address
            self.addressBook[scope][type] += 1

            return address
        
        else:
            raise semanticError(f'❌ Exceeded memory for <{type}> variables in <{scope}> scope')
        
    def allocateMemory(self, type, scope):
        # Build address | Base address based on scope & Type address
        address = self.buildAddress(type, scope)

        return address

    def resetContextAddresses(self):
        # Reset context bound address counters
        self.addressBook['local']['int']   = 0
        self.addressBook['local']['float'] = 4000
        self.addressBook['local']['bool']  = 8000
        self.addressBook['temp']['int']    = 0
        self.addressBook['temp']['float']  = 4000
        self.addressBook['temp']['bool']   = 8000
