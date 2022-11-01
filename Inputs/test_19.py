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


class TestInput19:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_19.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO',    -1,    -1,     2),
            ('='   , 40000,    -1, 10000),
            ('P'   ,    -1,    -1, 10000),
            ('='   , 40001,    -1, 10001),
            ('P'   ,    -1,    -1, 47500),
            ('P'   ,    -1,    -1, 10001),
            ('+'   , 10000, 10001, 30000),
            ('='   , 30000,    -1, 10002),
            ('R'   ,    -1,    -1, 10003),
            ('R'   ,    -1,    -1, 10004),
            ('R'   ,    -1,    -1, 10005),
            ('='   , 40002,    -1, 10006),
            ('='   , 40003,    -1, 10007),
            ('='   , 40004,    -1, 10008),
            ('*'   , 10000, 10001, 30001),
            ('*'   , 10003, 10005, 30002),
            ('/'   , 30002, 10006, 34000),
            ('+'   , 10002, 34000, 34001),
            ('+'   , 34001, 10007, 34002),
            ('/'   , 30001, 34002, 34003),
            ('-'   , 34003, 10008, 34004),
            ('+'   , 10000, 10001, 30003),
            ('*'   , 30003, 10002, 30004),
            ('-'   , 30004, 10003, 30005),
            ('>'   , 34004, 30005, 38000),
            ('='   , 38000,    -1, 18000),
            ('P'   ,    -1,    -1, 47501),
            ('P'   ,    -1,    -1, 18000),
        ]

        assert self.parser.QM.quadruples == quads
