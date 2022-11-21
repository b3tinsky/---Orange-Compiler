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

class TestInput31:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_31.txt')

    @pytest.mark.order(44)
    def test_execution(self):
        vm31 = VirtualMachine()
        vm31.run()

        result = [{10000: 1, 10001: None, 10010: 2, 10011: None, 10046: 3, 10047: None, 10002: None, 10003: None, 10004: None, 10005: None, 10006: None, 10007: None, 10008: None, 10009: None, 10012: None, 10013: None, 10014: None, 10015: None, 10016: None, 10017: None, 10018: None, 10019: None, 10020: None, 10021: None, 10022: None, 10023: 999, 10024: None, 10025: None, 10026: None, 10027: None, 10028: None, 10029: None, 10030: None, 10031: None, 10032: None, 10033: None, 10034: None, 10035: None, 10036: None, 10037: None, 10038: None, 10039: None, 10040: None, 10041: None, 10042: None, 10043: None, 10044: None, 10045: None, 10048: None, 10049: None, 10050: None, 10051: None, 10052: None, 10053: None, 10054: None, 10055: None, 10056: None, 10057: None, 10058: None, 10059: None, 10060: None, 10061: None, 10062: None, 10063: None}, {50000: 10023, 50001: 10023, 50002: 10023, 30000: 3, 30001: 21, 30002: 3, 30003: 24, 30004: 12, 30005: 3, 30006: 21, 30007: 3, 30008: 24, 30009: 12, 30010: 3, 30011: 21, 30012: 3, 30013: 24, 30014: 12, 30015: 998001}]

        assert vm31.memory == result