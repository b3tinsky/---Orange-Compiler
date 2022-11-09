# import os
# import sys
# import pytest
# from pathlib import Path
# from Components.scanner import OrangeLexer
# from Components.parser import OrangeParser
# from Components.status import OrangeStatus, lexicalError, syntacticalError, semanticError
# from Components.memory import MemoryManager
# from Components.virtualmachine import VirtualMachine

# def initializeCompiler(test_file):
#     testing_dir_path = str(Path.cwd() / Path('Inputs'))
#     input_dir = os.listdir(testing_dir_path)
#     file_path = testing_dir_path + '/' + test_file
#     file = open(file_path, 'r')
#     data = file.read()
#     file.close()
#     status = OrangeStatus()
#     memory = MemoryManager()
#     lexer = OrangeLexer(status)
#     parser = OrangeParser(status, memory)
#     parser.parse(lexer.tokenize(data))
#     return status, lexer, parser


# class TestInput28:
#     # Initialize a different compiler with the needed file
#     status, lexer, parser = initializeCompiler('input_28.txt')

#     def test_QUADGENERATION(self):
#         quads = [
#             ('GOTO', '', '', 31), 
#             ('>', 'a', 0, 'T1'), 
#             ('GOTOF', 'T1', '', 11), 
#             ('*', 'b', 'j', 'T2'), 
#             ('+', 'a', 'T2', 'T3'), 
#             ('+', 'T3', 'i', 'T4'), 
#             ('=', 'T4', '', 'i'), 
#             ('+', 'i', 'j', 'T5'), 
#             ('P', '', '', 'T5'), 
#             ('GOTO', '', '', 13), 
#             ('+', 'a', 'b', 'T6'), 
#             ('P', '', '', 'T6'), 
#             ('ENDFUNC', '', '', ''), 
#             ('=', 'a', '', 'i'), 
#             ('>', 'a', 0, 'T7'), 
#             ('GOTOF', 'T7', '', 30), 
#             ('*', 'k', 'j', 'T8'), 
#             ('-', 'a', 'T8', 'T9'), 
#             ('=', 'T9', '', 'a'), 
#             ('ERA', '', '', 'uno'), 
#             ('*', 'a', 2, 'T10'), 
#             ('PARAM', 'T10', '', 'P1'), 
#             ('+', 'a', 'k', 'T11'), 
#             ('PARAM', 'T11', '', 'P2'), 
#             ('GOSUB', '', '', 'uno'), 
#             ('*', 'g', 'j', 'T12'), 
#             ('-', 'T12', 'k', 'T13'), 
#             ('=', 'T13', '', 'g'), 
#             ('GOTO', '', '', 15), 
#             ('ENDFUNC', '', '', ''), 
#             ('=', 2, '', 'i'), 
#             ('+', 'i', 1, 'T14'), 
#             ('=', 'T14', '', 'k'), 
#             ('=', 3.14, '', 'f'), 
#             ('ERA', '', '', 'dos'), 
#             ('+', 'i', 'k', 'T15'), 
#             ('PARAM', 'T15', '', 'P1'), 
#             ('*', 'f', 3, 'T16'), 
#             ('PARAM', 'T16', '', 'P2'), 
#             ('GOSUB', '', '', 'dos'), 
#             ('P', '', '', 'i'), 
#             ('*', 'j', 2, 'T17'), 
#             ('P', '', '', 'T17'), 
#             ('*', 'f', 2, 'T18'), 
#             ('+', 'T18', 1.5, 'T19'), 
#             ('P', '', '', 'T19'), 
#             ('/', 'k', 2, 'T20'), 
#             ('-', 'i', 'T20', 'T21'), 
#             ('=', 'T21', '', 'i'), 
#             ('>', 'i', 0, 'T22'), 
#             ('GOTOT', 'T22', '', 35)
#             ]

#         assert self.parser.QM.quadruples == quads
