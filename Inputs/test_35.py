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

class TestInput35:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_35.txt')

    @pytest.mark.order(48)
    def test_execution(self):
        vm35 = VirtualMachine()
        vm35.run()

        result = [{}, {20000: 5, 20001: 3, 20002: 7, 20003: None, 20004: 6, 20005: 1, 20006: 2, 20007: 3, 20008: 4, 20009: 5, 20010: None, 20011: None, 20012: None, 20013: None, 20014: None, 20015: None, 50000: 20009, 50001: 20005, 50002: 20006, 50003: 20007, 50004: 20008, 50005: 20009, 30000: 6, 30001: 4, 30002: 0, 30003: 1, 30004: 2, 30005: 3, 30006: 4, 38000: False}]

        assert vm35.memory == result