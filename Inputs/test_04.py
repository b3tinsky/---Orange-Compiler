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

# DOC: In the testing document, add the expected directory
class TestInput04:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_04.txt')

    @pytest.mark.order(6)
    def test_VARDECLARATION(self):
        dir = {
            'test_4': {
                'name': 'test_4',
                'params':{},
                'quadruple': 1,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 3,
                        'int': 5
                    },
                    'params':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'temp':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'pointers': []
                },
                'table': {
                    'x': {
                        'address': 14000,
                        'dimensions': [],
                        'name': 'x', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'y': {
                        'address': 14001,
                        'dimensions': [],
                        'name': 'y', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'z': {
                        'address': 14002,
                        'dimensions': [],
                        'name': 'z', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'i': {
                        'address': 10004,
                        'dimensions': [],
                        'name': 'i', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 10000,
                        'dimensions': [],
                        'name': 'a',
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001,
                        'dimensions': [],
                        'name': 'b', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002,
                        'dimensions': [],
                        'name': 'c', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'd': {
                        'address': 10003,
                        'dimensions': [],
                        'name': 'd', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }
                    },
                'type': 'prog',
                }, 
            'main': {
                'name': 'main', 
                'params':{},
                'quadruple': 2,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 1
                    },
                    'params':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'temp':{
                        'bool': 0,
                        'float': 0,
                        'int': 2
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

    @pytest.mark.order(7)
    def test_constantsTable(self):
        constantsTable = {
            'bool': {},
            'float': {},
            'int': {
                1: 40000,
                2: 40001,
            },
            'string':{
                'Your result: ': 47500
            }
        }

        assert self.parser.OFD.constants == constantsTable

    @pytest.mark.order(8)
    def test_execution(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: 17)
        vm04 = VirtualMachine()
        vm04.run()

        result = [{10000: 1, 10001: 2, 10002: 3, 10003: 17, 10004: None, 14000: None, 14001: None, 14002: None}, {20000: None, 30000: 3, 30001: 20}]
        assert vm04.memory == result
