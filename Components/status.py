class OrangeStatus():
    def __init__(self) -> None:
        self.lexStatus      = '✅'
        self.syntaxStatus   = '✅'
        self.semanticStatus = '✅'

class lexicalError(Exception):
    pass

class syntacticalError(Exception):
    pass

class semanticError(Exception):
    pass