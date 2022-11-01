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

class TestInput27:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_27.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('='    , 40000,    -1, 10000),
            ('='    , 40000,    -1, 10001),
            ('='    , 40001,    -1, 10002),
            ('='    , 40000,    -1, 10003),
            ('='    , 40002,    -1, 10008),
            ('='    , 40003,    -1, 30000),
            ('<'    , 10008, 30000, 38000),
            ('GOTOF', 38000,    -1,    24),
            ('P'    ,    -1,    -1, 47500),
            ('P'    ,    -1,    -1, 10008),
            ('+'    , 10000, 10001, 30001),
            ('*'    , 10002, 10003, 30002),
            ('>'    , 30001, 30002, 38001),
            ('GOTOF', 38001,    -1,    20),
            ('P'    ,    -1,    -1, 47501),
            ('P'    ,    -1,    -1, 10008),
            ('+'    , 10001, 10003, 30003),
            ('='    , 30003,    -1, 10000),
            ('*'    , 10000, 10002, 30004),
            ('='    , 30004,    -1, 10001),
            ('++'   , 10008, 40001, 10008),
            ('GOTO' ,    -1,    -1,     8),
            ]

        assert self.parser.QM.quadruples == quads

    def test_execution(self):
        vm27 = VirtualMachine()
        vm27.run()

        result = [{18000: None, 18001: None, 18002: None, 10000: 22, 10001: 22, 10002: 1, 10003: 2, 10004: None, 10005: None, 10006: None, 10007: None, 10008: 10}, {30000: 10, 30001: 40, 30002: 2, 30003: 22, 30004: 22, 38000: False, 38001: True}]

        assert vm27.memory == result