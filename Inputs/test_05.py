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

class TestInput05:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_05.txt')
    
    @pytest.mark.order(9)
    def test_VARDECLARATION(self):
        dir = {
            'test_05': {
                'name': 'test_05', 
                'params': {},
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'int': 0, 
                        'float': 0, 
                        'bool': 0
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
                'table': {}, 
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
                    'result': {
                        'address': 20000, 
                        'name': 'result', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_a': {
                        'address': 20001, 
                        'name': 'sum_a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_b': {
                        'address': 20002, 
                        'name': 'sum_b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'void',
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 4, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
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
                    'test': {
                        'address': 20000,
                        'name': 'test', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    }, 
                'type': 'main',
                }
            }

        assert self.parser.OFD.dir == dir