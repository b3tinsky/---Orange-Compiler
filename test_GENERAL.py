import os
import sys
import pytest
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser
from Components.status import OrangeStatus, lexicalError, syntacticalError, semanticError

def initializeCompiler(test_file):
    testing_dir_path = str(Path.cwd() / Path('Inputs'))
    input_dir = os.listdir(testing_dir_path)
    file_path = testing_dir_path + '/' + test_file
    file = open(file_path, 'r')
    data = file.read()
    file.close()
    status = OrangeStatus()
    lexer = OrangeLexer(status)
    parser = OrangeParser(status)
    parser.parse(lexer.tokenize(data))
    return status, lexer, parser

class TestInput01:
    def test_exception_raised(self):
        with pytest.raises(syntacticalError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_01.txt')

class TestInput02:
    def test_exception_raised(self):
        with pytest.raises(lexicalError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_02.txt')

# DOC: In the testing document, add the expected directory
class TestInput03:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_03.txt')

    def test_VARDECLARATION(self):
        dir = {
            'main': {
                'name': 'main', 
                'type': 'main', 
                'quadruple': 1,
                'params':{},
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 3
                    },
                    'params':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'temp':{
                        'bool': 0,
                        'float': 0,
                        'int': 2
                    }
                },
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
                },

            'test_03': {
                'name': 'test_03', 
                'type': 'prog', 
                'table': {},
                'quadruple': 1,
                'params':{},
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'params':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    },
                    'temp':{
                        'bool': 0,
                        'float': 0,
                        'int': 0
                    }
                }
            }
        }
        assert self.parser.OFD.dir == dir

# DOC: In the testing document, add the expected directory
class TestInput04:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_04.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_4': {
                'name': 'test_4', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
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
                    'b': {
                        'name': 'b', 
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
                    },
                'quadruple': 0,
                'params':{},
                'signature':'',
                }
            }

        assert self.parser.OFD.dir == dir

# # DOC: In the testing document, add the expected directory
class TestInput05:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_05.txt')

    def test_VARDECLARATION(self):
        dir = {
            'sum': {
                'name': 'sum', 
                'type': 'void',
                'quadruple': 0,
                'params':{},
                'signature':'', 
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
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'test': {
                        'name': 'test', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                },
            'test_05': {
                'name': 'test_05', 
                'type': 'prog', 
                'table': {},
                'quadruple': 0,
                'params':{},
                'signature':'',
                }
            }

        assert self.parser.OFD.dir == dir

# DOC: In the testing document, add the expected directory
class TestInput06:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_06.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_06': {
                'name': 'test_06', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
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
                'quadruple': 0,
                'params':{},
                'signature':'',
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
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'test': {
                        'name': 'test', 
                        'type': 'int', 
                        'scope': 'main'
                        }
                    }
                },
            'test_06': {
                'name': 'test_06', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
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
                    'b': {
                        'name': 'b', 
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
            }
        }
        assert self.parser.OFD.dir == dir

# DOC: In the testing document, add the expected directory
class TestInput07:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_07.txt')

# DOC: In the testing document, add the expected directory
class TestInput08:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_08.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_08': {
                'name': 'test_08', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'global'
                    }, 
                    'b': {
                        'name': 'b', 
                        'type': 'int', 
                        'scope': 'global'
                    }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'global'
                    }
                }
            }, 
            'sum': {
                'name': 'sum', 
                'type': 'int', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'sum'
                    }, 
                    'b': {
                        'name': 'b', 
                        'type': 'int', 
                        'scope': 'sum'
                    }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'sum'
                    }
                }
            }, 
            'main': {
                'name': 'main', 
                'type': 'main', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'a': {
                        'name': 'a', 
                        'type': 'float', 
                        'scope': 'main'
                    }, 
                    'b': {
                        'name': 'b', 
                        'type': 'float', 
                        'scope': 'main'
                    }, 
                    'c': {
                        'name': 'c', 
                        'type': 'float', 
                        'scope': 'main'
                    }
                }
            }
        }
        assert self.parser.OFD.dir == dir

class TestInput09:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_09.txt')

# DOC: In the testing document, add the expected directory
class TestInput10:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_10.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_10': {
                'name': 'test_10', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'test_10': {
                        'name': 'test_10', 
                        'type': 'int', 'scope': 
                        'global'
                        }, 
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'b': {
                        'name': 'b', 
                        'type': 'int', 
                        'scope': 'global'
                    }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'global'
                    }
                }
            }, 
            'sum': {
                'name': 'sum', 
                'type': 'int', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'sum': {
                        'name': 'sum', 
                        'type': 'int', 
                        'scope': 'sum'
                    }, 
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'sum'
                    }, 
                    'b': {
                        'name': 'b', 
                        'type': 'int', 
                        'scope': 'sum'
                        }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'sum'
                    }
                }
            }, 
            'main': {
                'name': 'main', 
                'type': 'main', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'test_10': {
                        'name': 'test_10', 
                        'type': 'int', 
                        'scope': 'main'
                    }, 
                    'a': {
                        'name': 'a', 
                        'type': 'float', 
                        'scope': 'main'
                    }, 
                    'b': {
                        'name': 'b', 
                        'type': 'float', 
                        'scope': 'main'
                    }, 
                    'c': {
                        'name': 'c', 
                        'type': 'float', 
                        'scope': 'main'
                    }
                }
            }
        }
        assert self.parser.OFD.dir == dir

class TestInput11:
    def test_exception_raised(self):
        with pytest.raises(syntacticalError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_11.txt')

class TestInput12:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_12.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_12': {
                'name': 'test_12', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'a': {
                        'name': 'a', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'b': {
                        'name': 'b', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'c': {
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'global'
                        }
                    }
                }, 
                'sum': {
                    'name': 'sum', 
                    'type': 'int', 
                    'quadruple': 0,
                    'params':{},
                    'signature':'',
                    'table': {}
                }, 
                'main': {
                    'name': 'main', 
                    'type': 'main', 
                    'quadruple': 0,
                    'params':{},
                    'signature':'',
                    'table': {
                        'x': {
                            'name': 'x', 
                            'type': 'int', 
                            'scope': 'main'
                            }, 
                        'y': {
                            'name': 'y', 
                            'type': 'int', 
                            'scope': 'main'
                            }, 
                        'z': {
                            'name': 'z', 
                            'type': 'int', 
                            'scope': 'main'
                            }
                        }
                    }
                }

        assert self.parser.OFD.dir == dir

class TestInput13:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_13.txt')

class TestInput14:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_14.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_14': {
                'name': 'test_14', 
                'type': 'prog', 
                'quadruple': 0,
                'params':{},
                'signature':'',
                'table': {
                    'x': {
                        'name': 'x', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'y': {
                        'name': 'y', 
                        'type': 'int', 
                        'scope': 'global'
                        }, 
                    'z': {
                        'name': 'z', 
                        'type': 'int', 
                        'scope': 'global'
                        }
                    }
                }, 
                'sum': {
                    'name': 'sum', 
                    'type': 'int', 
                    'quadruple': 0,
                    'params':{},
                    'signature':'',
                    'table': {
                        'a': {
                            'name': 'a', 
                            'type': 'int', 
                            'scope': 'sum'
                            }, 
                        'b': {
                            'name': 'b', 
                            'type': 'int', 
                            'scope': 'sum'
                            }
                        }
                    }, 
                'main': {
                    'name': 'main', 
                    'type': 'main', 
                    'quadruple': 0,
                    'params':{},
                    'signature':'',
                    'table': {}
                    }
                }

        assert self.parser.OFD.dir == dir

class TestInput15:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_15.txt')

class TestInput16:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_16.txt')

class TestInput17:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_17.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('*', 'c', 'd', 'T1'), 
            ('+', 'b', 'T1', 'T2'), 
            ('-', 'T2', 'e', 'T3'),
            ('*', 'a', 'T3', 'T4'),
            ('*', 'c', 'd', 'T5'),
            ('-', 'T5', 'e', 'T6'),
            ('+', 'b', 'T6', 'T7'),
            ('>', 'T4', 'T7', 'T8'),
            ('=', 'T8', '', 'z')

        ]
        assert self.parser.QM.quadruples == quads

class TestInput18:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_18.txt')

    def test_QUADGENERATION(self):
        quads = [
           ('*', 'a', 'b', 'T1'),
           ('*', 'd', 'f', 'T2'),
           ('/', 'T2', 'g', 'T3'),
           ('+', 'c', 'T3', 'T4'),
           ('+', 'T4', 'h', 'T5'),
           ('/', 'T1', 'T5', 'T6'),
           ('-', 'T6', 'i', 'T7'),
           ('+', 'a', 'b', 'T8'),
           ('*', 'T8', 'c', 'T9'),
           ('-', 'T9', 'd', 'T10'),
           ('>', 'T7', 'T10', 'T11'),
           ('=', 'T11', '', 'z')
        ]

        assert self.parser.QM.quadruples == quads

class TestInput19:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_19.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('=', 1, '', 'a'),
            ('P', '', '', 'a'),
            ('=', 2, '', 'b'),
            ('P', '', '', 'b: '),
            ('P', '', '', 'b'),
            ('+', 'a', 'b', 'T1'),
            ('=', 'T1', '', 'c'),
            ('R', '', '', 'd'),
            ('R', '', '', 'e'),
            ('R', '', '', 'f'),
            ('=', 7, '', 'g'),
            ('=', 8, '', 'h'),
            ('=', 9, '', 'i'),
            ('*', 'a', 'b', 'T2'),
            ('*', 'd', 'f', 'T3'),
            ('/', 'T3', 'g', 'T4'),
            ('+', 'c', 'T4', 'T5'),
            ('+', 'T5', 'h', 'T6'),
            ('/', 'T2', 'T6', 'T7'),
            ('-', 'T7', 'i', 'T8'),
            ('+', 'a', 'b', 'T9'),
            ('*', 'T9', 'c', 'T10'),
            ('-', 'T10', 'd', 'T11'),
            ('>', 'T8', 'T11', 'T12'),
            ('=', 'T12', '', 'z'),
            ('P', '', '', 'Z: '),
            ('P', '', '', 'z')
        ]

        assert self.parser.QM.quadruples == quads

class TestInput20:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_20.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('+', 'a', 'b', 'T1'),
            ('*', 'c', 'd', 'T2'),
            ('>', 'T1', 'T2', 'T3'),
            ('GOTOF', 'T3', '', 7),
            ('+', 'b', 'd', 'T4'),
            ('=', 'T4', '', 'a'),
            ('*', 'a', 'c', 'T5'),
            ('=', 'T5', '', 'b'),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput21:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_21.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('+', 'a', 'b', 'T1'),
            ('*', 'c', 'd', 'T2'),
            ('>', 'T1', 'T2', 'T3'),
            ('GOTOF', 'T3', '', 8),
            ('+', 'b', 'd', 'T4'),
            ('=', 'T4', '', 'a'),
            ('GOTO', '', '', 10),
            ('-', 'd', 'c', 'T5'),
            ('=', 'T5', '', 'a'),
            ('*', 'a', 'c', 'T6'),
            ('+', 'T6', 'd', 'T7'),
            ('=', 'T7', '', 'b'),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput22:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_22.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('*', 'a', 'b', 'T1'),
            ('+', 'T1', 'c', 'T2'),
            ('-', 'd', 'e', 'T3'),
            ('>', 'T2', 'T3', 'T4'),
            ('GOTOF', 'T4', '', 17),
            ('*', 'd', 'c', 'T5'),
            ('+', 'c', 'T5', 'T6'),
            ('=', 'T6', '', 'b'),
            ('P', '', '', 'b'),
            ('+', 'a', 'b', 'T7'),
            ('P', '', '', 'T7'),
            ('>', 'a', 'b', 'T8'),
            ('GOTOF', 'T8', '', 16),
            ('+', 'd', 'e', 'T9'),
            ('=', 'T9', '', 'c'),
            ('GOTO', '', '', 20),
            ('+', 'b', 'c', 'T10'),
            ('=', 'T10', '', 'a'),
            ('P', '', '', 'a'),
            ('*', 'd', 'e', 'T11'),
            ('=', 'T11', '', 'c'),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput23:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_23.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('*', 'b', 'c', 'T1'),
            ('>', 'a', 'T1', 'T2'),
            ('GOTOF', 'T2', '', 8),
            ('-', 'a', 'd', 'T3'),
            ('=', 'T3', '', 'a'),
            ('P', '', '', 'a'),
            ('GOTO', '', '', 1),
            ('+', 'c', 'a', 'T4'),
            ('=', 'T4', '', 'b'),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput24:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_24.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('*', 'b', 'c', 'T1'),
            ('+', 'a', 'T1', 'T2'),
            ('<', 'T2', 'd', 'T3'),
            ('GOTOF', 'T3', '', 26),
            ('+', 'a', 'b', 'T4'),
            ('<', 'T4', 'c', 'T5'),
            ('GOTOF', 'T5', '', 16),
            ('+', 'b', 'c', 'T6'),
            ('=', 'T6', '', 'a'),
            ('-', 'a', 1, 'T7'),
            ('=', 'T7', '', 'a'),
            ('+', 'b', 'c', 'T8'),
            ('>', 'a', 'T8', 'T9'),
            ('GOTOT', 'T9', '', 10),
            ('GOTO', '', '', 25),
            ('+', 'c', 'd', 'T10'),
            ('>', 'b', 'T10', 'T11'),
            ('GOTOF', 'T11', '', 25),
            ('*', 'c', 'd', 'T12'),
            ('+', 'b', 'T12', 'T13'),
            ('=', 'T13', '', 'a'),
            ('-', 'a', 'd', 'T14'),
            ('=', 'T14', '', 'b'),
            ('GOTO', '', '', 16),
            ('GOTO', '', '', 1),
            ('*', 'b', 'c', 'T15'),
            ('=', 'T15', '', 'a'),
            ('=', 0, '', 'c')
        ]

        assert self.parser.QM.quadruples == quads

class TestInput25:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_25.txt')

class TestInput26:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_26.txt')

class TestInput27:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_27.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('=', 0, '', 'i'), 
            ('=', 10, '', 'T1'), 
            ('<', 'i', 'T1', 'T2'), 
            ('GOTOF', 'T2', '', 15), 
            ('+', 'a', 'b', 'T3'), 
            ('*', 'c', 'd', 'T4'), 
            ('>', 'T3', 'T4', 'T5'), 
            ('GOTOF', 'T5', '', 11), 
            ('+', 'b', 'd', 'T6'), 
            ('=', 'T6', '', 'a'), 
            ('*', 'a', 'c', 'T7'), 
            ('=', 'T7', '', 'b'), 
            ('++', 'i', 1, 'i'), 
            ('GOTO', '', '', 3)
            ]

        assert self.parser.QM.quadruples == quads

class TestInput28:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_28.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO', '', '', 31), 
            ('>', 'a', 0, 'T1'), 
            ('GOTOF', 'T1', '', 11), 
            ('*', 'b', 'j', 'T2'), 
            ('+', 'a', 'T2', 'T3'), 
            ('+', 'T3', 'i', 'T4'), 
            ('=', 'T4', '', 'i'), 
            ('+', 'i', 'j', 'T5'), 
            ('P', '', '', 'T5'), 
            ('GOTO', '', '', 13), 
            ('+', 'a', 'b', 'T6'), 
            ('P', '', '', 'T6'), 
            ('ENDFUNC', '', '', ''), 
            ('=', 'a', '', 'i'), 
            ('>', 'a', 0, 'T7'), 
            ('GOTOF', 'T7', '', 30), 
            ('*', 'k', 'j', 'T8'), 
            ('-', 'a', 'T8', 'T9'), 
            ('=', 'T9', '', 'a'), 
            ('ERA', '', '', 'uno'), 
            ('*', 'a', 2, 'T10'), 
            ('PARAM', 'T10', '', 'P1'), 
            ('+', 'a', 'k', 'T11'), 
            ('PARAM', 'T11', '', 'P2'), 
            ('GOSUB', '', '', 'uno'), 
            ('*', 'g', 'j', 'T12'), 
            ('-', 'T12', 'k', 'T13'), 
            ('=', 'T13', '', 'g'), 
            ('GOTO', '', '', 15), 
            ('ENDFUNC', '', '', ''), 
            ('=', 2, '', 'i'), 
            ('+', 'i', 1, 'T14'), 
            ('=', 'T14', '', 'k'), 
            ('=', 3.14, '', 'f'), 
            ('ERA', '', '', 'dos'), 
            ('+', 'i', 'k', 'T15'), 
            ('PARAM', 'T15', '', 'P1'), 
            ('*', 'f', 3, 'T16'), 
            ('PARAM', 'T16', '', 'P2'), 
            ('GOSUB', '', '', 'dos'), 
            ('P', '', '', 'i'), 
            ('*', 'j', 2, 'T17'), 
            ('P', '', '', 'T17'), 
            ('*', 'f', 2, 'T18'), 
            ('+', 'T18', 1.5, 'T19'), 
            ('P', '', '', 'T19'), 
            ('/', 'k', 2, 'T20'), 
            ('-', 'i', 'T20', 'T21'), 
            ('=', 'T21', '', 'i'), 
            ('>', 'i', 0, 'T22'), 
            ('GOTOT', 'T22', '', 35)
            ]

        assert self.parser.QM.quadruples == quads