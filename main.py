from pathlib import Path
from lex import OrangeLexer
from parser import OrangeParser
import os



# ✅❌
testing_dir_path = str(Path.cwd() / Path('Testing/Inputs'))
input_dir = os.listdir(testing_dir_path)

def orange_juice(test_name, test_data):
    lexer = OrangeLexer()
    parser = OrangeParser()
    print('▼'*30, test_name ,'▼'*30)
    for tok in lexer.tokenize(test_data):
        print('type=%r, value=%r' % (tok.type, tok.value))
        
    result = parser.parse(lexer.tokenize(test_data))
    print('-'*21)
    print('Intended Status: ✅ |')
    print(f'Reported Status: {parser.status} |')
    print('▲'*30, test_name ,'▲'*30)
    print()

for input_file in input_dir:
    file_path = testing_dir_path + '/' + input_file
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    orange_juice(input_file, data)