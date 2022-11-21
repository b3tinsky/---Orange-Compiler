# Add components in top directory so they can  be imported
    # in other subdirectories
from Components.funcdir import OrangeFuncDir
from Components.vartable import OrangeVarTable
from Components.status import OrangeStatus
from Components.memory import MemoryManager
from Components.virtualmachine import VirtualMachine

# Normal imports
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser
import os
import sys

def orange_juice(test_name, test_data):
    try:
        lexer = OrangeLexer(StatusChecker)
        parser = OrangeParser(StatusChecker, MemoryM)
        parser.parse(lexer.tokenize(test_data))
        
    except Exception as err:
        print(str(err))

    parser.OFD.printdata() # HACK: Prints Function Directory
    print(f'-'*50)
    print('JUMPS: ', parser.QM.jumps)
    print('OPERANDS: ', parser.QM.operands)
    print('OPERATORS: ', parser.QM.operators)
    print(f'-'*50)
    parser.QM.printQuads() # HACK: Prints Quadruples
    print(f'-'*50)
    # print('▲'*15, test_name ,'▲'*15)
    VM.run()


# Persistent Objects
StatusChecker = OrangeStatus()
MemoryM = MemoryManager()
VM = VirtualMachine()

# Command line arguments
argument_list = sys.argv[1:]

# Options
arguments_short = ['lp']
arguments_long = ['lex', 'parser']

testing_dir_path = str(Path.cwd())
input_dir = os.listdir(testing_dir_path)

# RUN DEVELOPMENT INPUT
file_path = testing_dir_path + f'/{argument_list[0]}'
file = open(file_path, 'r')
data = file.read()
file.close()
orange_juice(argument_list[0], data)