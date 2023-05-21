class _notImplemented(Exception):
    def __str__(self):
        return 'Not implemented'

class _noEnd(Exception):
    def __str__(self):
        return '\033[38;5;14mUNENDING PAIN AND SUFFERING'

class _undeclaredVar(Exception):
    def __init__(self, var):
        super().__init__()
        self.var = var

    def __str__(self):
        return f"\033[38;5;14m{self.var} WASN'T NOTICED"

class _capError(Exception):
    def __str__(self):
        return "\033[38;5;14mSYNTAX ERROR"

class _jumpError(Exception):
      def __init__(self, cond,symbol_table):
        self.cond=cond
        self.symbol_table=symbol_table

      def __str__(self):
        return f"\033[38;5;14mSOMETHING WENT WRONG EVALUATING: {self.cond}\nHERE IS THE CURRENT SYMBOL TABLE:\n {self.symbol_table}"

class _noLabel(Exception):
    def __init__(self, label):
        self.label=label
      
    def __str__(self):
        return f"\033[38;5;14mUNKNOWN MARKING: {self.label}"

class _noStart(Exception):
    def __str__(self):
        return "\033[38;5;14mWHEN DID IT EVEN START"

class _noBoop(Exception):
    def __str__(self):
        return "\033[38;5;14mFAILED TO BOOP THE USER"

class _tooManyBoop(Exception):
    def __str__(self):
        return "\033[38;5;14mTOO MANY BOOPS!"

class _castingFail(Exception):
    def __str__(self):
        return "\033[38;5;14mTRANSFORMATION FAILED"

class _unmatchedComment(Exception):
    def __str__(self):
        return "\033[38;5;14mWHICH IS BETTER? PAWS OR MAWS?"

class _importError(Exception):
    def __init__(self, module):
        self.module=module
      
    def __str__(self):
        return f"\033[38;5;14mUNKNOWN MODULE: {self.module}"

class _alreadyImported(Exception):
    def __str__(self):
        return "\033[38;5;14mYOU ALREADY DRAGGED IT! WHY WASTE EFFORT?"
    
class _undefinedKeyword(Exception):
    def __init__(self, imported,line,symbols):
        self.imported=imported
        self.line=line
        self.symbol_table=symbols
    def __str__(self):
        return f"\033[38;5;14mUNKNOWN KEYWORD {self.line}:\nDEBUG CODE!\nIMPORTED MODULES:{self.imported}\nTABLE:{self.symbol_table}"
    
class _debug(Exception):
    def __init__(self, imported,line,symbols):
        self.imported=imported
        self.line=line
        self.symbol_table=symbols
    def __str__(self):
        return f"\033[38;5;14mDEBUG CODE!\nCURRENT LINE:{self.line}\nIMPORTED MODULES:{self.imported}\nTABLE:{self.symbol_table}"