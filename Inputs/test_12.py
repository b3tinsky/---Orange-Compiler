import os
import sys
import pytest
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser
from Components.status import OrangeStatus, lexicalError, syntacticalError, semanticError
from Components.memory import MemoryManager
from Components.virtualmachine import VirtualMachine

def initializeCompiler(test_file):
    testing_dir_path = str(Path.cwd() / Path('Inputs'))
    input_dir = os.listdir(testing_dir_path)
    file_path = testing_dir_path + '/' + test_file
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    status = OrangeStatus()
    memory = MemoryManager()
    lexer = OrangeLexer(status)
    parser = OrangeParser(status, memory)
    parser.parse(lexer.tokenize(data))
    return status, lexer, parser

class TestInput12:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_12.txt')
    
    @pytest.mark.order(17)
    def test_VARDECLARATION(self):
        dir = {
            'test_12': {
                'name': 'test_12', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 10000, 
                        'name': 'a', 
                        'scope': 'test_12',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001, 
                        'name': 'b', 
                        'scope': 'test_12',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002, 
                        'name': 'c', 
                        'scope': 'test_12',
                        'type': 'int', 
                        },
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_12',
                        'type': 'int', 
                        },
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 2, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {}, 
                'type': 'int', 
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 6, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {
                    'x': {
                        'address': 20000, 
                        'name': 'x', 
                        'scope': 'main',
                        'type': 'int', 
                        }, 
                    'y': {
                        'address': 20001, 
                        'name': 'y', 
                        'scope': 'main',
                        'type': 'int', 
                        }, 
                    'z': {
                        'address': 20002, 
                        'name': 'z', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    }, 
                'type': 'main', 
                }
            }

        assert self.parser.OFD.dir == dir