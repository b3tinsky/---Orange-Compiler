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

class TestInput22:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_22.txt')
    
    @pytest.mark.order(31)
    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('*'    , 10000, 10001, 30000),
            ('+'    , 30000, 10002, 30001),
            ('-'    , 10003, 10004, 30002),
            ('>'    , 30001, 30002, 38000),
            ('GOTOF', 38000,    -1,    18),
            ('*'    , 10003, 10002, 30003),
            ('+'    , 10002, 30003, 30004),
            ('='    , 30004,    -1, 10001),
            ('P'    ,    -1,    -1, 10001),
            ('+'    , 10000, 10001, 30005),
            ('P'    ,    -1,    -1, 30005),
            ('>'    , 10000, 10001, 38001),
            ('GOTOF', 38001,    -1,    17),
            ('+'    , 10003, 10004, 30006),
            ('='    , 30006,    -1, 10002),
            ('GOTO' ,    -1,    -1,    21),
            ('+'    , 10001, 10002, 30007),
            ('='    , 30007,    -1, 10000),
            ('P'    ,    -1,    -1, 10000),
            ('*'    , 10003, 10004, 30008),
            ('='    , 30008,    -1, 10002),
        ]

        assert self.parser.QM.quadruples == quads
