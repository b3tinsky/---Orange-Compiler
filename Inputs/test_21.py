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

class TestInput21:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_21.txt')
    
    @pytest.mark.order(29)
    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('='    , 40000,    -1, 10000),
            ('='    , 40001,    -1, 10001),
            ('='    , 40002,    -1, 10002),
            ('='    , 40000,    -1, 10003),
            ('+'    , 10000, 10001, 30000),
            ('*'    , 10002, 10003, 30001),
            ('>'    , 30000, 30001, 38000),
            ('GOTOF', 38000,    -1,    13),
            ('+'    , 10001, 10003, 30002),
            ('='    , 30002,    -1, 10000),
            ('GOTO' ,    -1,    -1,    15),
            ('-'    , 10003, 10002, 30003),
            ('='    , 30003,    -1, 10000),
            ('*'    , 10000, 10002, 30004),
            ('+'    , 30004, 10003, 30005),
            ('='    , 30005,    -1, 10001),
            ('P'    ,    -1,    -1, 47500),
            ('P'    ,    -1,    -1, 10000),
        ]

        assert self.parser.QM.quadruples == quads

    @pytest.mark.order(30)
    def test_execution(self):
        vm21 = VirtualMachine()
        vm21.run()

        result = [{18000: None, 18001: None, 18002: None, 10000: -2, 10001: -5, 10002: 3, 10003: 1, 10004: None, 10005: None, 10006: None, 10007: None, 10008: None}, {30000: 3, 30001: 3, 30002: None, 30003: -2, 30004: -6, 30005: -5, 38000: False}]

        assert vm21.memory == result