blue='\033[38;5;14m'
from random import randint
class _notImplemented(Exception):
    def __str__(self):
        return 'Not implemented'

class _noEnd(Exception):
    def __str__(self):
        case = randint(0,1)
        if case == 0:
            return blue+"UNENDING PAIN AND SUFFERING"
        if case == 1:
            return blue+"WHEN WILL IT EVER END"
class _undeclaredVar(Exception):
    def __init__(self, var):
        super().__init__()
        self.var = var

    def __str__(self):
        case = randint(0,2)
        if case == 0:
            return blue+f"{self.var} WASN'T NOTICED"
        if case == 1:
            return blue+f"CAN'T FIND {self.var}, DID YOU CHECK THE BALLPIT?"
        if case == 2:
            return blue+f"MAYBE {self.var} IS AT THE HOTEL"

class _capError(Exception):
    def __str__(self):
        case = randint(0,3)
        if case == 0:
            return blue+"i cantz undertsands u!!"
        if case == 1:
            return blue+"SPEAK FURRY OR DON'T SPEAK AT ALL"
        if case == 2:
            return blue+"TAKE OFF YOUR FURSUIT HEAD I CAN'T HEAR YOU"
        if case == 3:
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
        case = randint(0,3)
        if case == 0:
            return blue+"I APPEAR TO BE LOST"
        if case == 1:
            return blue+"LOST IN THE BALLPIT"
        if case == 2:
            return blue+"WHERE AM I SUPPOSED TO GO?"
        if case == 3:
            return blue+f"UNKNOWN MARKING: {self.label}"
        

class _noStart(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:
            return blue+"WHAT AM I SUPPOSED TO DO?"
        if case == 1:
            return blue+"WHERE'S THE ENTRANCE"
        if case == 2:
            return blue+"WHEN DID IT EVEN START"

class _noBoop(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:
            return blue+"I CAN'T REACH YOUR SNOUT!!!"
        if case == 1:
            return blue+"BOOP INTERCEPTED"
        if case == 2:
            return blue+"FAILED TO BOOP THE USER"

class _tooManyBoop(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:
            return blue+"SENSORY OVERLOAD :("
        if case == 1:
            return blue+"TOO MANY BOOPS!"
        if case == 2:
            return blue+"WHY DO I HEAR MOANING"

class _castingFail(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:
            return blue+"TRANSFORMATION FAILED"
        if case == 1:
            return blue+"THE ETHICS COMMITTEE SAID NO"
        if case == 2:
            return blue+"PURO SAID NO"

class _unmatchedComment(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:
          return blue+"YOU'RE TOO QUIET SPEAK UP"
        if case == 1:
          return blue+"\"PERSONALITY\" ISN'T AN OPTION"
        if case == 2:
          return blue+"WHICH IS BETTER? PAWS OR MAWS?"

class _importError(Exception):
    def __init__(self, module):
        self.module=module
      
    def __str__(self):
        case = randint(0,2)
        if case == 0:  
            return blue+f"UNKNOWN MODULE: {self.module}"
        if case == 1:
            return blue+f"{self.module} WASN'T AT THE HOTEL"
        if case == 2:
            return blue+f"{self.module} WASN'T AT THE CON"
            
class _alreadyImported(Exception):
    def __str__(self):
        case = randint(0,5)
        if case == 0:
            return blue+"YOU ALREADY DRAGGED IT! WHY WASTE EFFORT?"
        if case == 1:
            return blue+"TOO TIRED"
        if case == 2:
            return blue+"IT SAID \"NO CAMERAS ALLOWED\"!"
        if case == 3:
            return blue+"I ALREADY PAID FOR THIS CON"
        if case == 4:
            return blue+"MY LEGS HURT"
        if case == 5:
            return blue+"WHERE ARE YOU DRAGGING ME TO?"
        
class _divideByZero(Exception):
    def __str__(self):
        case = randint(0,2)
        if case == 0:  
            return blue+f"THE UNIVERSE EXPLODED."
        if case == 1:
            return blue+f"PUPPY BRAIN CAN'T DO MATH"
        if case == 2:
            return blue+"Sorry, I was in the bathroom. What'd I mi- Where'd... Where is everyone?"

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
