import os
import sys
import pytest
from pathlib import Path
from Components.scanner import OrangeLexer
from Components.parser import OrangeParser
from Components.status import OrangeStatus, lexicalError, syntacticalError, semanticError
from Components.memory import MemoryManager

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

    def test_functionDirectory(self):
        dir = {
            'main': {
                'name': 'main', 
                'params':{},
                'type': 'main', 
                'quadruple': 1,
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
                    'x': {
                        'address': 20002,
                        'name': 'x', 
                        'scope': 'main',
                        'type': 'int', 
                        },
                    'y': {
                        'address': 20000, 
                        'name': 'y', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    'z': {
                        'address': 20001, 
                        'name': 'z', 
                        'type': 'int', 
                        'scope': 'main'
                        }, 
                    }
                },

            'test_03': {
                'name': 'test_03', 
                'params':{},
                'quadruple': 1,
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
                },
                'type': 'prog', 
                'table': {},
            }
        }
        assert self.parser.OFD.dir == dir

    def test_constantsTable(self):
        constantsTable = {
            'bool': {},
            'float': {},
            'int': {
                1: 40000,
                2: 40001,
                11: 40002
            },
            'string':{
                'Your result: ': 47500
            }
}

        assert self.parser.OFD.constants == constantsTable


# DOC: In the testing document, add the expected directory
class TestInput04:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_04.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_4': {
                'name': 'test_4',
                'params':{},
                'quadruple': 1,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 3,
                        'int': 5
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
                },
                'table': {
                    'x': {
                        'address': 14000,
                        'name': 'x', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'y': {
                        'address': 14001,
                        'name': 'y', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'z': {
                        'address': 14002,
                        'name': 'z', 
                        'scope': 'test_4',
                        'type': 'float', 
                        }, 
                    'i': {
                        'address': 10000,
                        'name': 'i', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 10001,
                        'name': 'a',
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10002,
                        'name': 'b', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10003,
                        'name': 'c', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }, 
                    'd': {
                        'address': 10004,
                        'name': 'd', 
                        'scope': 'test_4',
                        'type': 'int', 
                        }
                    },
                'type': 'prog',
                }, 
            'main': {
                'name': 'main', 
                'params':{},
                'quadruple': 1,
                'signature':'',
                'size':{
                    'local':{
                        'bool': 0,
                        'float': 0,
                        'int': 1
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
                    'test': {
                        'address': 20000, 
                        'name': 'test', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    },
                'type': 'main', 
                }
            }

        assert self.parser.OFD.dir == dir

    def test_constantsTable(self):
        constantsTable = {
            'bool': {},
            'float': {},
            'int': {
                1: 40000,
                2: 40001,
            },
            'string':{
                'Your result: ': 47500
            }
}

        assert self.parser.OFD.constants == constantsTable


# DOC: In the testing document, add the expected directory
class TestInput05:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_05.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_05': {
                'name': 'test_05', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'int': 0, 
                        'float': 0, 
                        'bool': 0
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {}, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '',
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'result': {
                        'address': 20000, 
                        'name': 'result', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_a': {
                        'address': 20001, 
                        'name': 'sum_a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_b': {
                        'address': 20002, 
                        'name': 'sum_b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'void',
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 4, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'test': {
                        'address': 20003, 
                        'name': 'test', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    }, 
                'type': 'main',
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
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 3, 
                        'int': 5, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'x': {
                        'address': 14000, 
                        'name': 'x', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'y': {
                        'address': 14001, 
                        'name': 'y', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'z': {
                        'address': 14002, 
                        'name': 'z', 
                        'scope': 'test_06',
                        'type': 'float', 
                        }, 
                    'i': {
                        'address': 10000, 
                        'name': 'i', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 10001, 
                        'name': 'a', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10002, 
                        'name': 'b', 
                        'scope': 'test_06',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10003, 
                        'name': 'c', 
                        'type': 'int', 
                        'scope': 'test_06'
                        }, 
                    'd': {
                        'address': 10004, 
                        'name': 'd', 
                        'type': 'int', 
                        'scope': 'test_06'
                        }
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum',
                'params': {},
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'result': {
                        'address': 20000, 
                        'name': 'result', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_a': {
                        'address': 20001, 
                        'name': 'sum_a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'sum_b': {
                        'address': 20002, 
                        'name': 'sum_b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'void', 
                }, 
            'main': {
                'name': 'main',
                'params': {},
                'quadruple': 3,
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 2, 
                        }
                    },
                'table': {
                    'test': {
                        'address': 20003, 
                        'name': 'test', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    },
                'type': 'main',
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
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 10000, 
                        'name': 'a', 
                        'scope': 'test_08',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001, 
                        'name': 'b', 
                        'scope': 'test_08',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002, 
                        'name': 'c', 
                        'scope': 'test_08',
                        'type': 'int', 
                        },
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_08',
                        'type': 'int', 
                        },
                    }, 
                'type': 'prog'
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 20000, 
                        'name': 'a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 20001, 
                        'name': 'b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 20002, 
                        'name': 'c', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'int', 

                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 7, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 3, 
                        'int': 0, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 1, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 24000, 
                        'name': 'a', 
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'b': {
                        'address': 24001, 
                        'name': 'b', 
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'c': {
                        'address': 24002, 
                        'name': 'c', 
                        'scope': 'main',
                        'type': 'float', 
                        }
                    }, 
                'type': 'main', 
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
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 4, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'test_10': {
                        'address': 10000, 
                        'name': 'test_10', 
                        'scope': 'test_10',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 10001, 
                        'name': 'a', 
                        'scope': 'test_10',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10002, 
                        'name': 'b', 
                        'scope': 'test_10',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10003, 
                        'name': 'c', 
                        'scope': 'test_10',
                        'type': 'int', 
                        },
                    'sum': {
                        'address': 10004, 
                        'name': 'sum', 
                        'scope': 'test_10',
                        'type': 'int', 
                        },
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 4, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {
                    'sum': {
                        'address': 20000, 
                        'name': 'sum', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 20001, 
                        'name': 'a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 20002, 
                        'name': 'b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 20003, 
                        'name': 'c', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'int', 
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 7, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 3, 
                        'int': 1, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 1, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'test_10': {
                        'address': 20004, 
                        'name': 'test_10', 
                        'scope': 'main',
                        'type': 'int', 
                        }, 
                    'a': {
                        'address': 24000, 
                        'name': 'a', 
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'b': {
                        'address': 24001, 
                        'name': 'b', 
                        'scope': 'main',
                        'type': 'float', 
                        }, 
                    'c': {
                        'address': 24002, 
                        'name': 'c', 
                        'scope': 'main',
                        'type': 'float', 
                        }
                    }, 

                'type': 'main'
                }
            }
        assert self.parser.OFD.dir == dir

class TestInput11:
    def test_exception_raised(self):
        with pytest.raises(syntacticalError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_11.txt')

# DOC: In the testing document, add the expected directory
class TestInput12:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_12.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_12': {
                'name': 'test_12', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 10000, 
                        'name': 'a', 
                        'scope': 'test_12',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 10001, 
                        'name': 'b', 
                        'scope': 'test_12',
                        'type': 'int', 
                        }, 
                    'c': {
                        'address': 10002, 
                        'name': 'c', 
                        'scope': 'test_12',
                        'type': 'int', 
                        },
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_12',
                        'type': 'int', 
                        },
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 2, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {}, 
                'type': 'int', 
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 7, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {
                    'x': {
                        'address': 20000, 
                        'name': 'x', 
                        'scope': 'main',
                        'type': 'int', 
                        }, 
                    'y': {
                        'address': 20001, 
                        'name': 'y', 
                        'scope': 'main',
                        'type': 'int', 
                        }, 
                    'z': {
                        'address': 20002, 
                        'name': 'z', 
                        'scope': 'main',
                        'type': 'int', 
                        }
                    }, 
                'type': 'main', 
                }
            }

        assert self.parser.OFD.dir == dir

class TestInput13:
    def test_exception_raised(self):
        with pytest.raises(semanticError):
            # Initialize a different compiler with the needed file
            status, lexer, parser = initializeCompiler('input_13.txt')

# DOC: In the testing document, add the expected directory
class TestInput14:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_14.txt')

    def test_VARDECLARATION(self):
        dir = {
            'test_14': {
                'name': 'test_14', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 3, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }
                    },
                'table': {
                    'sum': {
                        'address': 10003, 
                        'name': 'sum', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'x': {
                        'address': 10000, 
                        'name': 'x', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'y': {
                        'address': 10001, 
                        'name': 'y', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }, 
                    'z': {
                        'address': 10002, 
                        'name': 'z', 
                        'scope': 'test_14',
                        'type': 'int', 
                        }
                    }, 
                'type': 'prog', 
                }, 
            'sum': {
                'name': 'sum', 
                'params': {}, 
                'quadruple': 1, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 2, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {
                    'a': {
                        'address': 20000, 
                        'name': 'a', 
                        'scope': 'sum',
                        'type': 'int', 
                        }, 
                    'b': {
                        'address': 20001, 
                        'name': 'b', 
                        'scope': 'sum',
                        'type': 'int', 
                        }
                    }, 
                'type': 'int', 
                }, 
            'main': {
                'name': 'main', 
                'params': {}, 
                'quadruple': 8, 
                'signature': '', 
                'size': {
                    'local': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'params': {
                        'bool': 0,
                        'float': 0, 
                        'int': 0, 
                        }, 
                    'temp': {
                        'bool': 0,
                        'float': 0, 
                        'int': 1, 
                        }
                    },
                'table': {}, 
                'type': 'main', 
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
            ('GOTO',    -1,    -1,     2),
            ('*'   , 10002, 10003, 30000), 
            ('+'   , 10001, 30000, 30001), 
            ('-'   , 30001, 10004, 30002),
            ('*'   , 10000, 30002, 30003),
            ('*'   , 10002, 10003, 30004),
            ('-'   , 30004, 10004, 30005),
            ('+'   , 10001, 30005, 30006),
            ('>'   , 30003, 30006, 38000),
            ('='   , 38000,    -1, 18000)
        ]
        assert self.parser.QM.quadruples == quads

class TestInput18:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_18.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO',    -1,    -1,     2),
            ('*'   , 10000, 10001, 30000),
            ('*'   , 10003, 10005, 30001),
            ('/'   , 30001, 10006, 34000),
            ('+'   , 10002, 34000, 34001),
            ('+'   , 34001, 10007, 34002),
            ('/'   , 30000, 34002, 34003),
            ('-'   , 34003, 10008, 34004),
            ('+'   , 10000, 10001, 30002),
            ('*'   , 30002, 10002, 30003),
            ('-'   , 30003, 10003, 30004),
            ('>'   , 34004, 30004, 38000),
            ('='   , 38000,    -1, 18000),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput19:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_19.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO',    -1,    -1,     2),
            ('='   , 40000,    -1, 10000),
            ('P'   ,    -1,    -1, 10000),
            ('='   , 40001,    -1, 10001),
            ('P'   ,    -1,    -1, 47500),
            ('P'   ,    -1,    -1, 10001),
            ('+'   , 10000, 10001, 30000),
            ('='   , 30000,    -1, 10002),
            ('R'   ,    -1,    -1, 10003),
            ('R'   ,    -1,    -1, 10004),
            ('R'   ,    -1,    -1, 10005),
            ('='   , 40002,    -1, 10006),
            ('='   , 40003,    -1, 10007),
            ('='   , 40004,    -1, 10008),
            ('*'   , 10000, 10001, 30001),
            ('*'   , 10003, 10005, 30002),
            ('/'   , 30002, 10006, 34000),
            ('+'   , 10002, 34000, 34001),
            ('+'   , 34001, 10007, 34002),
            ('/'   , 30001, 34002, 34003),
            ('-'   , 34003, 10008, 34004),
            ('+'   , 10000, 10001, 30003),
            ('*'   , 30003, 10002, 30004),
            ('-'   , 30004, 10003, 30005),
            ('>'   , 34004, 30005, 38000),
            ('='   , 38000,    -1, 18000),
            ('P'   ,    -1,    -1, 47501),
            ('P'   ,    -1,    -1, 18000),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput20:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_20.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('+'    , 10000, 10001, 30000),
            ('*'    , 10002, 10003, 30001),
            ('>'    , 30000, 30001, 38000),
            ('GOTOF', 38000,    -1,     8),
            ('+'    , 10001, 10003, 30002),
            ('='    , 30002,    -1, 10000),
            ('*'    , 10000, 10002, 30003),
            ('='    , 30003,    -1, 10001),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput21:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_21.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('+'    , 10000, 10001, 30000),
            ('*'    , 10002, 10003, 30001),
            ('>'    , 30000, 30001, 38000),
            ('GOTOF', 38000,    -1,     9),
            ('+'    , 10001, 10003, 30002),
            ('='    , 30002,    -1, 10000),
            ('GOTO' ,    -1,    -1,    11),
            ('-'    , 10003, 10002, 30003),
            ('='    , 30003,    -1, 10000),
            ('*'    , 10000, 10002, 30004),
            ('+'    , 30004, 10003, 30005),
            ('='    , 30005,    -1, 10001),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput22:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_22.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('*'    , 10000, 10001, 30000),
            ('+'    , 30000, 10002, 30001),
            ('-'    , 10003, 10004, 30002),
            ('>'    , 30001, 30002, 38000),
            ('GOTOF', 38000,    -1,    18),
            ('*'    , 10003, 10002, 30003),
            ('+'    , 10002, 30003, 30004),
            ('='    , 30004,    -1, 10001),
            ('P'    ,    -1,    -1, 10001),
            ('+'    , 10000, 10001, 30005),
            ('P'    ,    -1,    -1, 30005),
            ('>'    , 10000, 10001, 38001),
            ('GOTOF', 38001,    -1,    17),
            ('+'    , 10003, 10004, 30006),
            ('='    , 30006,    -1, 10002),
            ('GOTO' ,    -1,    -1,    21),
            ('+'    , 10001, 10002, 30007),
            ('='    , 30007,    -1, 10000),
            ('P'    ,    -1,    -1, 10000),
            ('*'    , 10003, 10004, 30008),
            ('='    , 30008,    -1, 10002),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput23:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_23.txt')

    def test_QUADGENERATION(self):
        quads = [
            ('GOTO' ,    -1,    -1,     2),
            ('*'    , 10001, 10002, 30000),
            ('>'    , 10000, 30000, 38000),
            ('GOTOF', 38000,    -1,     9),
            ('-'    , 10000, 10003, 30001),
            ('='    , 30001,    -1, 10000),
            ('P'    ,    -1,    -1, 10000),
            ('GOTO' ,    -1,    -1,     2),
            ('+'    , 10002, 10000, 30002),
            ('='    , 30002,    -1, 10001),
        ]

        assert self.parser.QM.quadruples == quads

class TestInput24:
    # Initialize a different compiler with the needed file
    status, lexer, parser = initializeCompiler('input_24.txt')

    def test_QUADGENERATION(self):
        quads = [
            ( 'GOTO' ,    -1,    -1,     2),
            ( '*'    , 10001, 10002, 30000),
            ( '+'    , 10000, 30000, 30001),
            ( '<'    , 30001, 10003, 38000),
            ( 'GOTOF', 38000,    -1,    27),
            ( '+'    , 10000, 10001, 30002),
            ( '<'    , 30002, 10002, 38001),
            ( 'GOTOF', 38001,    -1,    17),
            ( '+'    , 10001, 10002, 30003),
            ( '='    , 30003,    -1, 10000),
            ( '-'    , 10000, 40000, 30004),
            ( '='    , 30004,    -1, 10000),
            ( '+'    , 10001, 10002, 30005),
            ( '>'    , 10000, 30005, 38002),
            ( 'GOTOT', 38002,    -1,    11),
            ( 'GOTO' ,    -1,    -1,    26),
            ( '+'    , 10002, 10003, 30006),
            ( '>'    , 10001, 30006, 38003),
            ( 'GOTOF', 38003,    -1,    26),
            ( '*'    , 10002, 10003, 30007),
            ( '+'    , 10001, 30007, 30008),
            ( '='    , 30008,    -1, 10000),
            ( '-'    , 10000, 10003, 30009),
            ( '='    , 30009,    -1, 10001),
            ( 'GOTO' ,    -1,    -1,    17),
            ( 'GOTO' ,    -1,    -1,     2),
            ( '*'    , 10001, 10002, 30010),
            ( '='    , 30010,    -1, 10000),
            ( '='    , 40001,    -1, 10002),
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
            ('GOTO' ,    -1,    -1,     2),
            ('='    , 40000,    -1, 10008),
            ('='    , 40001,    -1, 30000),
            ('<'    , 10008, 30000, 38000),
            ('GOTOF', 38000,    -1,    16),
            ('+'    , 10000, 10001, 30001),
            ('*'    , 10002, 10003, 30002),
            ('>'    , 30001, 30002, 38001),
            ('GOTOF', 38001,    -1,    12),
            ('+'    , 10001, 10003, 30003),
            ('='    , 30003,    -1, 10000),
            ('*'    , 10000, 10002, 30004),
            ('='    , 30004,    -1, 10001),
            ('++'   , 10008, 40002, 10008),
            ('GOTO' ,    -1,    -1,     4),
            ]

        assert self.parser.QM.quadruples == quads

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

#     # TODO: Test for a typed function without a RETURN statement (throws error)