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

class TestInput20:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_20.txt')

    @pytest.mark.order(27)
    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('='    , 40000,    -1, 10000),
            ('='    , 40001,    -1, 10001),
            ('='    , 40001,    -1, 10002),
            ('='    , 40000,    -1, 10003),
            ('+'    , 10000, 10001, 30000),
            ('*'    , 10002, 10003, 30001),
            ('>'    , 30000, 30001, 38000),
            ('GOTOF', 38000,    -1,    12),
            ('+'    , 10001, 10003, 30002),
            ('='    , 30002,    -1, 10000),
            ('*'    , 10000, 10002, 30003),
            ('='    , 30003,    -1, 10001),
            ('P'    ,    -1,    -1, 47500),
            ('P'    ,    -1,    -1, 10000),
        ]

        assert self.parser.QM.quadruples == quads

    @pytest.mark.order(28)
    def test_execution(self):
        vm20 = VirtualMachine()
        vm20.run()

        result = [{18000: None, 18001: None, 18002: None, 10000: 3, 10001: 6, 10002: 2, 10003: 1, 10004: None, 10005: None, 10006: None, 10007: None, 10008: None}, {30000: 3, 30001: 2, 30002: 3, 30003: 6, 38000: True}]

        assert vm20.memory == result