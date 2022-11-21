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

class TestInput14:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_14.txt')
    @pytest.mark.order(19)
    def test_VARDECLARATION(self):
        dir = {
            'test_14': {
                'name': 'test_14', 
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
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'x': {
                        'address': 10000, 
                        'dimensions':[],
                        'name': 'x',
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'y': {
                        'address': 10001, 
                        'dimensions':[],
                        'name': 'y', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'z': {
                        'address': 10002, 
                        'dimensions':[],
                        'name': 'z', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 2, 
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
                        },
                    'pointers':[]
                    },
                'table': {}, 
                'type': 'main', 
                }
            }

        assert self.parser.OFD.dir == dir
