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

class TestInput29:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_29.txt')
    @pytest.mark.order(41)
    def test_QUADGENERATION(self):
        quads = [
            ('GOTO'   ,    -1,    -1,     14),
            ('=='     , 20000, 40000,  38000),
            ('GOTOF'  , 38000,    -1,      6),
            ('RETURN' , 20000,    -1,  10003),
            ('GOTO'   ,    -1,    -1,     13),
            ('ERA'    ,    -1,    -1, 'fact'),
            ('-'      , 20000, 40000,  30000),
            ('PARAM'  , 30000,    -1,      1),
            ('GOSUB'  ,    -1,    -1, 'fact'),
            ('='      , 10003,    -1,  30001),
            ('*'      , 20000, 30001,  30002),
            ('RETURN' , 30002,    -1,  10003),
            ('ENDFUNC',    -1,    -1,     -1),
            ('='      , 40001,    -1,  10000),
            ('='      , 40000,    -1,  10001),
            ('+'      , 10000, 40000,  30000),
            ('='      , 30000,    -1,  10002),
            ('='      , 42500,    -1,  14000),
            ('P'      ,    -1,    -1,  47500),
            ('ERA'    ,    -1,    -1, 'fact'),
            ('PARAM'  , 40002,    -1,      1),
            ('GOSUB'  ,    -1,    -1, 'fact'),
            ('='      , 10003,    -1,  30001),
            ('P'      ,    -1,    -1,  30001),
            ('P'      ,    -1,    -1,  47501)
            ]

        assert self.parser.QM.quadruples == quads
    
    @pytest.mark.order(42)
    def test_execution(self):
        vm29 = VirtualMachine()
        vm29.run()

        result = [{14000: 3.14, 10000: 2, 10001: 1, 10002: 3, 10003: 24}, {30000: 3, 30001: 24}]

        assert vm29.memory == result