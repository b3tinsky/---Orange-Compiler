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

class TestInput30:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_30.txt')
    @pytest.mark.order(43)    
    def test_execution(self):
        vm30 = VirtualMachine()
        vm30.run()

        result = [{10000: 1, 10001: None, 10010: 2, 10011: None, 10046: 3, 10047: None, 10002: None, 10003: None, 10004: 0, 10005: 1, 10006: 2, 10007: 3, 10008: 4, 10009: None, 10012: None, 10013: None, 10014: None, 10015: None, 10016: None, 10017: None, 10018: None, 10019: None, 10020: None, 10021: None, 10022: None, 10023: None, 10024: None, 10025: None, 10026: None, 10027: None, 10028: None, 10029: None, 10030: None, 10031: None, 10032: None, 10033: None, 10034: None, 10035: None, 10036: None, 10037: None, 10038: None, 10039: None, 10040: None, 10041: None, 10042: None, 10043: None, 10044: None, 10045: None, 10048: None, 10049: None, 10050: None, 10051: None, 10052: None, 10053: None, 10054: None, 10055: None, 10056: None, 10057: None, 10058: None, 10059: None, 10060: None, 10061: None, 10062: None, 10063: None}, {50000: 10004, 50001: 10005, 50002: 10006, 50003: 10007, 50004: 10008, 50005: 10004, 50006: 10005, 50007: 10006, 50008: 10007, 50009: 10008, 30000: 3, 30001: 4, 30002: 5, 30003: 6, 30004: 7, 30005: 3, 30006: 4, 30007: 5, 30008: 6, 30009: 7}]

        assert vm30.memory == result