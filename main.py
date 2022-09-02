from pathlib import Path
from lex import OrangeLexer

import os
# ✅❌
testing_dir_path = str(Path.cwd() / Path('Testing/Inputs'))
input_dir = os.listdir(testing_dir_path)

def orange_juice(test_name, test_data):
    print('▼'*30, test_name ,'▼'*30)
    scanner = OrangeLexer()
    scanner.build()
    scanner.test(test_data)
    # print('-'*21)
    # print('Intended Status: ✅ |')
    # print('Reported Status: ❌ |')
    print('▲'*30, test_name ,'▲'*30)

for input_file in input_dir:
    file_path = testing_dir_path + '/' + input_file
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    orange_juice(input_file, data)