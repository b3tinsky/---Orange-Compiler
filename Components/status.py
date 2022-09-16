class OrangeStatus():
    def __init__(self) -> None:
        self.lexStatus      = '✅'
        self.syntaxStatus   = '✅'
        self.semanticStatus = '✅'

    def lexError(self):
        self.lexStatus = '❌'
    
    def syntaxError(self):
        self.syntaxStatus = '❌'
    
    def semanticError(self):
        self.semanticStatus = '❌'
