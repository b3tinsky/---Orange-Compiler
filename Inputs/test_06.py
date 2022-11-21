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

class TestInput06:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_06.txt')
    
    @pytest.mark.order(10)
    def test_VARDECLARATION(self):
        dir = {
            'test_06': {
                'name': 'test_06', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 3, 
                        'int': 5, 
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
                    'x': {
                        'address': 14000, 
                        'dimensions':[],
                        'name': 'x', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'y': {
                        'address': 14001, 
                        'dimensions':[],
                        'name': 'y', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'z': {
                        'address': 14002, 
                        'dimensions':[],
                        'name': 'z', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'i': {
                        'address': 10004, 
                        'dimensions':[],
                        'name': 'i', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 10000, 
                        'dimensions':[],
                        'name': 'a', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001, 
                        'dimensions':[],
                        'name': 'b', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002, 
                        'dimensions':[],
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'test_06'
                        }, 
                    'd': {
                        'address': 10003, 
                        'dimensions':[],
                        'name': 'd', 
                        'type': 'int', 
                        'scope': 'test_06'
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
                    'result': {
                        'address': 20002, 
                        'dimensions':[],
                        'name': 'result', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_a': {
                        'address': 20000, 
                        'dimensions':[],
                        'name': 'sum_a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_b': {
                        'address': 20001, 
                        'dimensions':[],
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
                'quadruple': 3,
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
                        'int': 2, 
                        },
                    'pointers':[]
                    },
                'table': {
                    'test': {
                        'address': 20000, 
                        'dimensions':[],
                        'name': 'test', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    },
                'type': 'main',
                }
            }
        assert self.parser.OFD.dir == dir

    @pytest.mark.order(11)
    def test_execution(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: -3)
        vm06 = VirtualMachine()
        vm06.run()

        result = [{10000: 1, 10001: 2, 10002: 3, 10003: -3, 10004: None, 14000: None, 14001: None, 14002: None}, {20000: None, 30000: 3, 30001: 0}]
        assert vm06.memory == result