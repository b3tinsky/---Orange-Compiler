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

class TestInput23:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_23.txt')

    @pytest.mark.order(32)
    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('='    , 40000,    -1, 10000),
            ('='    , 40001,    -1, 10001),
            ('='    , 40002,    -1, 10002),
            ('='    , 40001,    -1, 10003),
            ('*'    , 10001, 10002, 30000),
            ('>'    , 10000, 30000, 38000),
            ('GOTOF', 38000,    -1,    13),
            ('-'    , 10000, 10003, 30001),
            ('='    , 30001,    -1, 10000),
            ('P'    ,    -1,    -1, 10000),
            ('GOTO' ,    -1,    -1,     6),
            # ('+'    , 10002, 10000, 30002),
            # ('='    , 30002,    -1, 10001),
        ]

        assert self.parser.QM.quadruples == quads

    @pytest.mark.order(33)
    def test_execution(self):
        vm23 = VirtualMachine()
        vm23.run()

        result = [{18000: None, 18001: None, 18002: None, 10000: 2, 10001: 2, 10002: 1, 10003: 2, 10004: None, 10005: None, 10006: None, 10007: None, 10008: None}, {30000: 2, 30001: 2, 38000: False}]

        assert vm23.memory == result