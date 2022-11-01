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

class TestInput18:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_18.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO',    -1,    -1,     2),
            ('='   , 40000,    -1, 10000),
            ('='   , 40001,    -1, 10001),
            ('='   , 40002,    -1, 10002),
            ('='   , 40003,    -1, 10003),
            ('='   , 40004,    -1, 10004),
            ('='   , 40003,    -1, 10005),
            ('='   , 40002,    -1, 10006),
            ('='   , 40001,    -1, 10007),
            ('='   , 40000,    -1, 10008),
            ('*'   , 10000, 10001, 30000),
            ('*'   , 10003, 10005, 30001),
            ('/'   , 30001, 10006, 34000),
            ('+'   , 10002, 34000, 34001),
            ('+'   , 34001, 10007, 34002),
            ('/'   , 30000, 34002, 34003),
            ('-'   , 34003, 10008, 34004),
            ('+'   , 10000, 10001, 30002),
            ('*'   , 30002, 10002, 30003),
            ('-'   , 30003, 10003, 30004),
            ('>'   , 34004, 30004, 38000),
            ('='   , 38000,    -1, 18000),
            ('P'   ,    -1,    -1, 47500),
            ('P'   ,    -1,    -1, 18000),
        ]

        assert self.parser.QM.quadruples == quads

    def test_execution(self):
        vm18 = VirtualMachine()
        vm18.run()

        result = [{18000: False, 10000: 1, 10001: 2, 10002: 3, 10003: 4, 10004: 5, 10005: 4, 10006: 3, 10007: 2, 10008: 1}, {30000: 2, 30001: 16, 30002: 3, 30003: 9, 30004: 5, 34000: 5.333333333333333, 34001: 8.333333333333332, 34002: 10.333333333333332, 34003: 0.19354838709677422, 34004: -0.8064516129032258, 38000: False}]

        assert vm18.memory == result