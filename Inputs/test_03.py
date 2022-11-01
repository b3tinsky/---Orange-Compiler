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

class TestInput03:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_03.txt')
    vm03 = VirtualMachine()
    vm03.run()

    def test_functionDirectory(self):
        dir = {
            'main': {
                'name': 'main', 
                'params':{},
                'type': 'main', 
                'quadruple': 1,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 3
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
                    }
                },
                'table': {
                    'x': {
                        'address': 20002,
                        'name': 'x', 
                        'scope': 'main',
                        'type': 'int', 
                        },
                    'y': {
                        'address': 20000, 
                        'name': 'y', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    'z': {
                        'address': 20001, 
                        'name': 'z', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    }
                },

            'test_03': {
                'name': 'test_03', 
                'params':{},
                'quadruple': 1,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
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
                    }
                },
                'type': 'prog', 
                'table': {},
            }
        }
        assert self.parser.OFD.dir == dir

    def test_constantsTable(self):
        constantsTable = {
            'bool': {},
            'float': {},
            'int': {
                1: 40000,
                2: 40001,
                11: 40002
            },
            'string':{
                'Your result: ': 47500
            }
}

        assert self.parser.OFD.constants == constantsTable

    def test_execution(self):
        result = [{}, {20000: 2, 20001: 3, 20002: 1, 30000: 3, 30001: 14}]

        assert self.vm03.memory == result