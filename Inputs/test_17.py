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

class TestInput17:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_17.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO',    -1,    -1,     2),
            ('='   , 40000,    -1, 10000),
            ('='   , 40001,    -1, 10001),
            ('='   , 40002,    -1, 10002),
            ('='   , 40001,    -1, 10003),
            ('='   , 40000,    -1, 10004),
            ('*'   , 10002, 10003, 30000), 
            ('+'   , 10001, 30000, 30001), 
            ('-'   , 30001, 10004, 30002),
            ('*'   , 10000, 30002, 30003),
            ('*'   , 10002, 10003, 30004),
            ('-'   , 30004, 10004, 30005),
            ('+'   , 10001, 30005, 30006),
            ('>'   , 30003, 30006, 38000),
            ('='   , 38000,    -1, 18000),
            ('P'   ,    -1,    -1, 47500),
            ('P'   ,    -1,    -1, 18000),
        ]
        assert self.parser.QM.quadruples == quads

    def test_execution(self):
        vm17 = VirtualMachine()
        vm17.run()

        result = [{14000: None, 18000: False, 10000: 1, 10001: 2, 10002: 3, 10003: 2, 10004: 1}, {30000: 6, 30001: 8, 30002: 7, 30003: 7, 30004: 6, 30005: 5, 30006: 7, 38000: False}]

        assert vm17.memory == result