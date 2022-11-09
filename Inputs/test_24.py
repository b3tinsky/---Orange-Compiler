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

class TestInput24:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_24.txt')
    
    @pytest.mark.order(34)
    def test_QUADGENERATION(self):
        quads = [
            ( 'GOTO' ,    -1,    -1,     2),
            ( '*'    , 10001, 10002, 30000),
            ( '+'    , 10000, 30000, 30001),
            ( '<'    , 30001, 10003, 38000),
            ( 'GOTOF', 38000,    -1,    27),
            ( '+'    , 10000, 10001, 30002),
            ( '<'    , 30002, 10002, 38001),
            ( 'GOTOF', 38001,    -1,    17),
            ( '+'    , 10001, 10002, 30003),
            ( '='    , 30003,    -1, 10000),
            ( '-'    , 10000, 40000, 30004),
            ( '='    , 30004,    -1, 10000),
            ( '+'    , 10001, 10002, 30005),
            ( '>'    , 10000, 30005, 38002),
            ( 'GOTOT', 38002,    -1,    11),
            ( 'GOTO' ,    -1,    -1,    26),
            ( '+'    , 10002, 10003, 30006),
            ( '>'    , 10001, 30006, 38003),
            ( 'GOTOF', 38003,    -1,    26),
            ( '*'    , 10002, 10003, 30007),
            ( '+'    , 10001, 30007, 30008),
            ( '='    , 30008,    -1, 10000),
            ( '-'    , 10000, 10003, 30009),
            ( '='    , 30009,    -1, 10001),
            ( 'GOTO' ,    -1,    -1,    17),
            ( 'GOTO' ,    -1,    -1,     2),
            ( '*'    , 10001, 10002, 30010),
            ( '='    , 30010,    -1, 10000),
            ( '='    , 40001,    -1, 10002),
        ]

        assert self.parser.QM.quadruples == quads
