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

class TestInput08:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_08.txt')
    @pytest.mark.order(13)
    def test_VARDECLARATION(self):
        dir = {
            'test_08': {
                'name': 'test_08', 
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
                        },
                    'pointers':[]
                    },
                'table': {
                    'a': {
                        'address': 10000, 
                        'dimensions':[], 
                        'name': 'a', 
                        'scope': 'test_08',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001, 
                        'dimensions':[], 
                        'name': 'b', 
                        'scope': 'test_08',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002, 
                        'dimensions':[], 
                        'name': 'c', 
                        'scope': 'test_08',
                        'type': 'int', 
                        },
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_08',
                        'type': 'int', 
                        },
                    }, 
                'type': 'prog'
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
                        },
                    'pointers':[]
                    },
                'table': {
                    'a': {
                        'address': 20000, 
                        'dimensions':[], 
                        'name': 'a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 20001, 
                        'dimensions':[], 
                        'name': 'b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 20002, 
                        'dimensions':[], 
                        'name': 'c', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'int', 

                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 7, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 3, 
                        'int': 0, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 1, 
                        'int': 0, 
                        },
                    'pointers':[]
                    },
                'table': {
                    'a': {
                        'address': 24000, 
                        'dimensions':[], 
                        'name': 'a',
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'b': {
                        'address': 24001, 
                        'dimensions':[], 
                        'name': 'b', 
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'c': {
                        'address': 24002, 
                        'dimensions':[], 
                        'name': 'c', 
                        'scope': 'main',
                        'type': 'float', 
                        }
                    }, 
                'type': 'main', 
                }
            }
        assert self.parser.OFD.dir == dir
