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

class TestInput28:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_28.txt')

    @pytest.mark.order(39)
    def test_QUADGENERATION(self):
        quads = [
             ('GOTO'   ,    -1,    -1,     5),
             ('+'      , 20000, 20001, 30000),
             ('RETURN' , 30000,    -1, 10003),
             ('ENDFUNC',    -1,    -1,    -1),
             ('='      , 40000,    -1, 10000),
             ('='      , 40001,    -1, 10001),
             ('+'      , 10000, 40001, 30000),
             ('='      , 30000,    -1, 10002),
             ('='      , 42500,    -1, 14000),
             ('P'      ,    -1,    -1, 47500),
             ('ERA'    ,    -1,    -1, 'sum'),
             ('PARAM'  , 40002,    -1,     1),
             ('PARAM'  , 40003,    -1,     2),
             ('GOSUB'  ,    -1,    -1, 'sum'),
             ('='      , 10003,    -1, 30001),
             ('P'      ,    -1,    -1, 30001),
             ('P'      ,    -1,    -1, 47501),
            ]

        assert self.parser.QM.quadruples == quads

    @pytest.mark.order(40)
    def test_execution(self):
        vm28 = VirtualMachine()
        vm28.run()

        result = [{14000: 3.14, 10000: 2, 10001: 1, 10002: 3, 10003: 12}, {30000: 3, 30001: 12}]

        assert vm28.memory == result