# Add components in top directory so they can  be imported
    # in other subdirectories
from Components.funcdir import OrangeFuncDir
from Components.vartable import OrangeVarTable
# from Components import funcdir
# from Components import vartable

# Normal imports
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser
import os
import sys

# Command line arguments
argument_list = sys.argv[1:]

# Options
arguments_short = ['lp']
arguments_long = ['lex', 'parser']

testing_dir_path = str(Path.cwd() / Path('Inputs'))
input_dir = os.listdir(testing_dir_path)

def orange_juice(test_name, test_data):
    # Original status ✅❌
    try:
        lexer = OrangeLexer()
        parser = OrangeParser()
        print('▼'*30, test_name ,'▼'*30)
        lexer_status = '🚸'
        parser_status = '🚸'
        
        # No command line arguments given
        if not argument_list:
                # for tok in lexer.tokenize(test_data):
                #     print('type=%r, value=%r' % (tok.type, tok.value))
                parser.parse(lexer.tokenize(test_data))
                lexer_status = lexer.ERROR_STATUS
                parser_status = parser.status
        
        # Command line arguments provided
        else:
            for arg in argument_list:
                # Only checks the lexer
                if arg == 'l':
                    for tok in lexer.tokenize(test_data):
                        print('type=%r, value=%r' % (tok.type, tok.value))
                        lexer_status = lexer.ERROR_STATUS
                
                # Only checks the parser
                elif arg == 'p':
                    result = parser.parse(lexer.tokenize(test_data))
                    parser_status = parser.status
        
                # Check both lexer and parser
                elif arg == 'lp' or arg == 'pl':
                    for tok in lexer.tokenize(test_data):
                        print('type=%r, value=%r' % (tok.type, tok.value))
                    result = parser.parse(lexer.tokenize(test_data))
                    lexer_status = lexer.ERROR_STATUS
                    parser_status = parser.status
        
        

    except Exception as err:
        print(str(err))

    parser.OFD.printdata()
    print('-'*21)
    # print('Intended Status: ✅ |')
    print(f'Lexical Status:  {lexer_status} |')
    print(f'Syntax  Status:  {parser_status} |')
    print('▲'*30, test_name ,'▲'*30)
    print()

# RUN ALL INPUTS
# for input_file in input_dir:
#     file_path = testing_dir_path + '/' + input_file
#     file = open(file_path, 'r')
#     data = file.read()
#     file.close()
#     orange_juice(input_file, data)

# RUN DEVELOPMENT INPUT
file_path = testing_dir_path + '/input_0.txt'
file = open(file_path, 'r')
data = file.read()
file.close()
orange_juice('input_0.txt', data)
