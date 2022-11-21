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

class TestInput32:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_32.txt')

    @pytest.mark.order(45)
    def test_execution(self):
        vm32 = VirtualMachine()
        vm32.run()

        result = [{10000: 2, 10001: 1, 10002: 3, 14000: 3.14, 10003: 6}, {30000: 3, 30001: 24, 30002: 6, 30003: 30}]

        assert vm32.memory == result