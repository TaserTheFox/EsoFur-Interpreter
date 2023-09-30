blue='\033[38;5;14m'
from random import randint
class _notImplemented(Exception):
    def __str__(self):
        return 'Not implemented'

class _noEnd(Exception):
    def __str__(self):
        return blue+'UNENDING PAIN AND SUFFERING'

class _undeclaredVar(Exception):
    def __init__(self, var):
        super().__init__()
        self.var = var

    def __str__(self):
        return blue+f"{self.var} WASN'T NOTICED"

class _capError(Exception):
    def __str__(self):
        return blue+"SYNTAX ERROR"

class _jumpError(Exception):
      def __init__(self, cond,symbol_table):
        self.cond=cond
        self.symbol_table=symbol_table

      def __str__(self):
        return blue+f"SOMETHING WENT WRONG EVALUATING: {self.cond}\nHERE IS THE CURRENT SYMBOL TABLE:\n {self.symbol_table}"

class _noLabel(Exception):
    def __init__(self, label):
        self.label=label
      
    def __str__(self):
        return blue+f"UNKNOWN MARKING: {self.label}"

class _noStart(Exception):
    def __str__(self):
        return blue+"WHEN DID IT EVEN START"

class _noBoop(Exception):
    def __str__(self):
        return blue+"FAILED TO BOOP THE USER"

class _tooManyBoop(Exception):
    def __str__(self):
        return blue+"TOO MANY BOOPS!"

class _castingFail(Exception):
    def __str__(self):
        return blue+"TRANSFORMATION FAILED"

class _unmatchedComment(Exception):
    def __str__(self):
        return blue+"WHICH IS BETTER? PAWS OR MAWS?"

class _importError(Exception):
    def __init__(self, module):
        self.module=module
      
    def __str__(self):
        case = randint(0,1)
        if case == 0:  
            return blue+f"UNKNOWN MODULE: {self.module}"
        if case == 1:
            return blue+f"{self.module} WASN'T AT THE CON"
class _alreadyImported(Exception):
    def __str__(self):
        case = randint(0,1)
        if case == 0:
            return blue+"YOU ALREADY DRAGGED IT! WHY WASTE EFFORT?"
        if case == 1:
            return blue+"TOO TIRED"
class _undefinedKeyword(Exception):
    def __init__(self, imported,line,symbols):
        self.imported=imported
        self.line=line
        self.symbol_table=symbols
    def __str__(self):
        return blue+f"UNKNOWN KEYWORD {self.line}:\nDEBUG CODE!\nIMPORTED MODULES:{self.imported}\nTABLE:{self.symbol_table}"
    
class _debug(Exception):
    def __init__(self, imported,line,symbols):
        self.imported=imported
        self.line=line
        self.symbol_table=symbols
    def __str__(self):
        return blue+f"DEBUG CODE!\nCURRENT LINE:{self.line}\nIMPORTED MODULES:{self.imported}\nTABLE:{self.symbol_table}"