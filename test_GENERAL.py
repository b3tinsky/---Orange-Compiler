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
                'table': {}
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
                    }
                }
            }

        assert self.parser.OFD.dir == dir

# DOC: In the testing document, add the expected directory
class TestInput05:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_05.txt')

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
                },
            'test_05': {
                'name': 'test_05', 
                'type': 'prog', 
                'table': {}
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
                },
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
                    'table': {}
                }, 
                'main': {
                    'name': 'main', 
                    'type': 'main', 
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
            ('>', 'T4', 'T7', 'T8')
            ]
        assert self.parser.QM.quadruples == quads
