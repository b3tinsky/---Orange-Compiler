from Components.status import semanticError

class MemoryManager():
    
    def __init__(self):
        self.programName = '' # Global scope
    
        # Base addresses
        self.global_base   = 10000
        self.local_base    = 20000
        self.temp_base     = 30000
        self.const_base    = 40000
        self.pointers_base = 50000
        
        # Main typed addresses
        self.main_int      = 0
        self.main_float    = 4000
        self.main_bool     = 8000
        
        # Constant fixed addresses
        self.const_int     = 0
        self.const_float   = 2500
        self.const_bool    = 5000
        self.const_string  = 7500

        self.addressBook = {
            'global': {
                'base'  : self.global_base,     # Base Address
                'int'   : self.main_int,        # Range for ints    10,000 - 13,999
                'float' : self.main_float,      # Range for floats  14,000 - 17,999
                'bool'  : self.main_bool        # Range for bools   18,000 - 19,999
            },
            'local': {
                'base'  : self.local_base,      # Base Address
                'int'   : self.main_int,        # Range for ints    20,000 - 23,999
                'float' : self.main_float,      # Range for floats  24,000 - 27,999
                'bool'  : self.main_bool        # Range for bools   28,000 - 29,999
            },
            'temp': {
                'base'  : self.temp_base,       # Base Address
                'int'   : self.main_int,        # Range for ints    30,000 - 33,999
                'float' : self.main_float,      # Range for floats  34,000 - 37,999
                'bool'  : self.main_bool        # Range for bools   38,000 - 39,999
            },
            'const': {
                'base'   : self.const_base,     # Base Address
                'int'    : self.const_int,      # Range for ints    40,000 - 42,499
                'float'  : self.const_float,    # Range for floats  42,500 - 44,999
                'bool'   : self.const_bool,     # Range for bools   45,000 - 47,499
                'string' : self.const_string    # Range for strings 47,500 - 49,999                
            },     
            'pointers': {
                'base'   : self.pointers_base,  # Base Address
                'int'    : self.main_int        # Range for ints    50,000 - 59,999
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
            ('global', 'int'   )  : lambda: self.global_base                     <= self.addressBook['global'  ]['base'] + self.addressBook['global'  ]['int'   ] < self.global_base   + self.main_float,
            ('global', 'float' )  : lambda: self.global_base + self.main_float   <= self.addressBook['global'  ]['base'] + self.addressBook['global'  ]['float' ] < self.global_base   + self.main_bool,
            ('global', 'bool'  )  : lambda: self.global_base + self.main_bool    <= self.addressBook['global'  ]['base'] + self.addressBook['global'  ]['bool'  ] < self.local_base,
            ('local' , 'int'   )  : lambda: self.local_base                      <= self.addressBook['local'   ]['base'] + self.addressBook['local'   ]['int'   ] < self.local_base    + self.main_float,
            ('local' , 'float' )  : lambda: self.local_base  + self.main_float   <= self.addressBook['local'   ]['base'] + self.addressBook['local'   ]['float' ] < self.local_base    + self.main_bool,
            ('local' , 'bool'  )  : lambda: self.local_base  + self.main_bool    <= self.addressBook['local'   ]['base'] + self.addressBook['local'   ]['bool'  ] < self.temp_base,
            ('temp'  , 'int'   )  : lambda: self.temp_base                       <= self.addressBook['temp'    ]['base'] + self.addressBook['temp'    ]['int'   ] < self.temp_base     + self.main_float,
            ('temp'  , 'float' )  : lambda: self.temp_base   + self.main_float   <= self.addressBook['temp'    ]['base'] + self.addressBook['temp'    ]['float' ] < self.temp_base     + self.main_bool,
            ('temp'  , 'bool'  )  : lambda: self.temp_base   + self.main_bool    <= self.addressBook['temp'    ]['base'] + self.addressBook['temp'    ]['bool'  ] < self.const_base,
            ('const' , 'int'   )  : lambda: self.const_base                      <= self.addressBook['const'   ]['base'] + self.addressBook['const'   ]['int'   ] < self.const_base    + self.const_float,
            ('const' , 'float' )  : lambda: self.const_base  + self.const_float  <= self.addressBook['const'   ]['base'] + self.addressBook['const'   ]['float' ] < self.const_base    + self.const_bool,
            ('const' , 'bool'  )  : lambda: self.const_base  + self.const_bool   <= self.addressBook['const'   ]['base'] + self.addressBook['const'   ]['bool'  ] < self.const_base    + self.const_string,
            ('const' , 'string')  : lambda: self.const_base  + self.const_string <= self.addressBook['const'   ]['base'] + self.addressBook['const'   ]['string'] < self.pointers_base,
            ('pointers' , 'int')  : lambda: self.pointers_base                   <= self.addressBook['pointers']['base'] + self.addressBook['pointers']['int'   ] < 60000
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
        self.addressBook['local']['int']     = self.main_int
        self.addressBook['local']['float']   = self.main_float
        self.addressBook['local']['bool']    = self.main_bool
        self.addressBook['temp']['int']      = self.main_int
        self.addressBook['temp']['float']    = self.main_float
        self.addressBook['temp']['bool']     = self.main_bool
        self.addressBook['pointers']['int']  = self.main_int
