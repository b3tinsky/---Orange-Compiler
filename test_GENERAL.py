import os
import sys
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser


def initializeCompiler(test_file):
    testing_dir_path = str(Path.cwd() / Path('Inputs'))
    input_dir = os.listdir(testing_dir_path)
    file_path = testing_dir_path + '/' + test_file
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    lexer = OrangeLexer()
    parser = OrangeParser()
    parser.parse(lexer.tokenize(data))
    return lexer, parser

class TestInput01:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_01.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '❌'

class TestInput02:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_02.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '❌'

    def test_SYNTAX(self):
        assert self.parser.status == '❌'
    
class TestInput03:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_03.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'
    
    def test_VARDECLARATION(self):
        dir = {
            'main': {
                'name': 'main', 
                'type': 'main', 
                'table': {
                    'y': {
                        'name': 'y', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    'z': {
                        'name': 'z', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    'x': {
                        'name': 'x', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                }
            }
        assert self.parser.OFD.dir == dir

class TestInput04:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_04.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'
    
    def test_VARDECLARATION(self):
        dir = {
            'test_4': {
                'name': 'test_4', 
                'type': 'prog', 
                'table': {
                        'x': {
                            'name': 'x', 
                            'type': 'float', 
                            'scope': 'global'
                            }, 
                        'y': {
                            'name': 'y', 
                            'type': 'float', 
                            'scope': 'global'
                            }, 
                        'z': {
                            'name': 'z', 
                            'type': 'float', 
                            'scope': 'global'
                            }, 
                        'i': {
                            'name': 'i', 
                            'type': 'int', 
                            'scope': 'global'
                            }, 
                        'a': {
                            'name': 'a', 
                            'type': 'int', 
                            'scope': 'global'
                            }, 
                        'c': {
                            'name': 'c', 
                            'type': 'int', 
                            'scope': 'global'
                            }, 
                        'd': {
                            'name': 'd', 
                            'type': 'int', 
                            'scope': 'global'
                            }
                    }
                }, 
            'main': {
                'name': 'main', 
                'type': 'main', 
                'table': {
                    'test': {
                        'name': 'test', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                }
            }

        assert self.parser.OFD.dir == dir

class TestInput05:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_05.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'
    
    def test_VARDECLARATION(self):
        dir = {
            'sum': {
                'name': 'sum', 
                'type': 'void', 
                'table': {
                    'result': {
                        'name': 'result', 
                        'type': 'int', 
                        'scope': 'sum'
                        }, 
                    'sum_a': {
                        'name': 'sum_a', 
                        'type': 'int', 
                        'scope': 'sum'
                        }, 
                    'sum_b': {
                        'name': 'sum_b', 
                        'type': 'int', 
                        'scope': 'sum'
                        }
                    }
                }, 
            'main': {
                'name': 'main', 
                'type': 'main', 
                'table': {
                    'test': {
                        'name': 'test', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                }
            }

        assert self.parser.OFD.dir == dir

class TestInput06:
    # Initialize a different compiler with the needed file
    lexer, parser = initializeCompiler('input_06.txt')

    def test_LEX(self):
        assert self.lexer.ERROR_STATUS == '✅'

    def test_SYNTAX(self):
        assert self.parser.status == '✅'
    
    def test_VARDECLARATION(self):
        dir = {
            'test_06': {
                'name': 'test_06', 
                'type': 'prog', 
                'table': {
                    'x': {
                        'name': 'x', 
                        'type': 'float', 
                        'scope': 'global'
                        }, 
                    'y': {
                        'name': 'y', 
                        'type': 'float', 
                        'scope': 'global'
                        }, 
                    'z': {
                        'name': 'z', 
                        'type': 'float', 
                        'scope': 'global'
                        }, 
                    'i': {
                        'name': 'i', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'd': {
                        'name': 'd', 
                        'type': 'int', 
                        'scope': 'global'
                        }
                    }
                }, 
            'sum': {
                'name': 'sum', 
                'type': 'void', 
                'table': {
                    'result': {
                        'name': 'result', 
                        'type': 'int', 
                        'scope': 'sum'
                        }, 
                    'sum_a': {
                        'name': 'sum_a', 
                        'type': 'int', 
                        'scope': 'sum'
                        }, 
                    'sum_b': {
                        'name': 'sum_b', 
                        'type': 'int', 
                        'scope': 'sum'
                        }
                    }
                }, 
            'main': {
                'name': 'main', 
                'type': 'main', 
                'table': {
                    'test': {
                        'name': 'test', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                }
            }

        assert self.parser.OFD.dir == dir

# class TestInput07:
#     # Initialize a different compiler with the needed file
#     lexer, parser = initializeCompiler('input_07.txt')


#     def test_LEX(self):
#         assert self.lexer.ERROR_STATUS == '✅'

#     def test_SYNTAX(self):
#         assert self.parser.status == '✅'
    
#     def test_VARDECLARATION(self):
#         dir = {}

#         assert self.parser.OFD.dir == dir