import os
import sys
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser


class TestInput01:
    testing_dir_path = str(Path.cwd() / Path('Inputs'))
    input_dir = os.listdir(testing_dir_path)
    file_path = testing_dir_path + '/input_01.txt'
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    lexer = OrangeLexer()
    parser = OrangeParser()
    parser.parse(lexer.tokenize(data))


    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'

class TestInput02:
    testing_dir_path = str(Path.cwd() / Path('Inputs'))
    input_dir = os.listdir(testing_dir_path)
    file_path = testing_dir_path + '/input_02.txt'
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    lexer = OrangeLexer()
    parser = OrangeParser()
    parser.parse(lexer.tokenize(data))


    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'
    