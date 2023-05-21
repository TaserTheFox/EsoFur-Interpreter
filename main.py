import math,sys
from exceptions import _debug,_undefinedKeyword,_alreadyImported,_importError,_noEnd,_undeclaredVar,_capError,_jumpError,_noLabel
from exceptions import _noStart,_noBoop,_tooManyBoop,_castingFail,_unmatchedComment
class EsoFurCompiler:
    def __init__(self):
        self.symbol_table = {}
        self.in_comment = False
        self.imported = []
        self.imported_local=[]
    def compile(self, code):
        lines = code.split('\n')
        i = 0
        built=False
        module=''
        global done
        done = sys.exit  # Create an alias for sys.exit()
        if lines.count("Maws") != lines.count("Paws"):
            raise _unmatchedComment()
        while i < len(lines):
            line = lines[i].strip()

            # Skip empty lines
            if not line:
                i+=1
                continue

            # Check if program should run at all
            if line == "OwO What's This?":
                built=True
                i+=1
                continue

            elif not built:
                exit(0)

            # End of program
            if line=="QwQ":
                exit("\033[38;5;15mfinished")

            if "QwQ" not in lines:
                raise _noEnd()

            # Comment handling
            if line.startswith('Muzzles'):
                i+=1
                continue

            if line == "Maws":
                if self.in_comment == True:
                    raise _unmatchedComment()
                self.in_comment = True
                i+=1
                continue

            if line == "Paws":
                if self.in_comment == False:
                    raise _unmatchedComment()
                self.in_comment = False
                i+=1
                continue

            if self._in_comment == True:
                i+=1
                continue

            # Marking a line
            if line.startswith("Marks"):
                i+=1
                continue

            # Syntax check
            if line.istitle()==False:
                raise _capError()
            
            # Importing Esofur modules
            if line.startswith("Drag"):
                parse=line.split() #drag [function] from [module]
                if parse[2]!="From":
                    raise _capError()
                try:
                    if parse[1]=="Everything":
                        if parse[3] in self.imported:
                            raise _alreadyImported()
                        module += '\n' + self.grabfile(parse[3])
                        self.imported += [parse[3]]
                    else:
                        if parse[3]+'.'+parse[1] in self.imported_local:
                            raise _alreadyImported()
                        if parse[3] in self.imported_local:
                            raise _alreadyImported()
                        module += '\n' + self.grabfile(parse[3],parse[1])
                        self.imported_local += [parse[3]+'.'+parse[1]]
                        self.imported += [parse[3]]
                except _alreadyImported:
                    raise _alreadyImported()
                except:
                    raise _importError(parse[3])
                i+=1
                continue

            try:
                parse_value=self._parse_value
                for mod in self.imported_local:
                    if line.startswith(mod):
                        line=line.split('.')[1]
                        break
                exec(module,globals(),locals())
            except SystemExit:
                i+=1
                continue
            except:
                quit("SOMETHING WENT HORRIBLY WRONG")

            # Variable declaration
            if line.startswith('Notices Your'):
                var_name = line.split(' ')[2]
                self.symbol_table.update({var_name:None})
                i+=1
                continue

            # Assignment
            if 'Pounces On' in line:
                value, var_name = line.split('Pounces On')
                var_name = var_name.strip()
                if var_name not in self.symbol_table:
                    raise _undeclaredVar(var_name)
                value = self._assign(value.strip())
                self.symbol_table[var_name] = value
                i+=1
                continue

            # Jumps
            if 'Nuzzles' in line:
                if line.startswith("Nuzzles")==False:
                    condition, label = line.split('Nuzzles')
                    condition = self._parse_value(condition.strip())  # evaluate condition
                    #label = label.strip()
                    label = self._assign(label.strip())
                    if bool(condition):  # use bool() to convert the parsed condition to a boolean
                        if label.isdigit():
                            i+=label
                            continue
                        i = int(self._find_label_index(lines, label))
                    else:
                        i+=1
                else:
                    label =  self._assign(line.split()[1].strip())
                    if type(label)==int:
                        i+=label
                        continue
                    i = int(self._find_label_index(lines, label))
                continue


            # Loops
            if line == '*Starts Roleplaying*':
                i+=1
                continue

            if line.startswith('*Stops Roleplaying Because Of') and line.endswith('*'):
                condition = line.split(' ')[-1][:-1].strip()
                condition = self._parse_value(condition)
                if bool(condition):
                    i = self._find_loop_start_index(lines, i)
                else:
                    i+=1
                continue

            # Print
            if line.startswith('Howl'):
                var_name = line.split(' ')[1]
                value = self._assign(var_name.strip())
                print(value)
                i+=1
                continue

            # Ask user for input
            if line.startswith('Boop The User For'):
                text=line.split()
                var_name = text[4]
                prompt=':'
                if len(text) == 7:
                    if text[5]!='With':
                        raise _noBoop()
                    prompt=self._assign(text[6])+':'
                if len(text) > 7:
                    raise _tooManyBoop()
                value = input(prompt)
                value = self._assign(value)
                self.symbol_table[var_name] = value
                i+=1
                continue


            # Type casting
            if 'Transforms Into' in line:
                var_name, type_name = line.split('Transforms Into')
                var_name = var_name.strip()
                type_name = type_name.strip()
                value = self._parse_value(var_name)
                self.symbol_table[var_name] = self._cast_value(value, type_name)
                i+=1
                continue

            # Maths
            if 'Inflates By' in line:
                self._do_maths(line, "Inflates By", "+")
                i+=1
                continue

            if 'Pays' in line:
                self._do_maths(line, 'Pays', '-')
                i += 1
                continue

            if 'Breeds By' in line:
                self._do_maths(line, 'Breeds By', '*')
                i += 1
                continue

            if 'Baps' in line:
                self._do_maths(line, 'Baps', '/')
                i += 1
                continue

            if 'Deflates By' in line:
                self._do_maths(line, 'Deflates By', '%')
                i += 1
                continue

            if 'Gets Vored By' in line:
                self._do_maths(line, 'Gets Vored By', 'l')
                i += 1
                continue

            if 'Hyper-Inflates By' in line:
                self._do_maths(line, 'Hyper-Inflates By', '^')
                i += 1
                continue

            # UNDEFINED INSTRUCTIONS
            raise _undefinedKeyword(self.imported,line,self.symbol_table)

    def _find_label_index(self, lines, label):
        for i, line in enumerate(lines):
            if line.startswith('Marks') and line.split(' ')[1] == label:
                return i
        raise _noLabel(label)
        #print(f"Error: Label not found: {label}")

    def _find_loop_start_index(self, lines, end_index):
        loop_count=0
        for i in range(end_index - 1, -1, -1):
            if lines[i].startswith('*Stops Roleplaying Because Of') and lines[i].endswith('*'):
                loop_count+=1
            if lines[i] == '*Starts Roleplaying*':
                if loop_count == 0:
                    return i
                else:
                    loop_count-=1
        raise _noStart()

    def _assign(self, value_str):
        if value_str.isdigit():
            return int(value_str)
        if '"' in value_str:
            return value_str[value_str.find('"')+1:value_str.rfind('"')]
        elif value_str in self.symbol_table:
            return self.symbol_table[value_str]
        else:
            return value_str

    def _parse_value(self, value_str):
        if value_str.isdigit():
            return int(value_str)
        if value_str in self.symbol_table:
            return self.symbol_table[value_str]
        try:
            return eval(value_str, {}, self.symbol_table)
        except:
            raise _jumpError()

    def _cast_value(self, value, type_name):
        if type_name == 'Int':
            return int(value)
        if type_name == 'Float':
            return float(value)
        if type_name == 'Str':
            return str(value)
        if type_name == 'List':
            return list(value)
        if type_name == 'Furpile':
            return set(value)
        raise _castingFail()

    def _do_maths(self, line, keyword, operation):
        var_1, var_2 = map(lambda x: x.strip(), line.split(keyword))
        num_1 = self._parse_value(var_1)
        num_2 = self._parse_value(var_2)
        if operation == '+':
            num_1 += num_2
        if operation == '-':
            num_1 -= num_2
        if operation == '*':
            num_1 *= num_2
        if operation == '/':
            num_1 = num_2 / num_1
        if operation == '%':
            num_1 %= num_2
        if operation == 'l':
            num_1 = math.log(num_1, num_2)
        if operation == '^':
            num_1 **= num_2
        self.symbol_table[var_1] = num_1

    def grabfile(self, module, *word):
        with open(module+'.EsoMod', "r") as file:
            source_code = file.read()
        if len(word)==0:
            return source_code
        else:
            source_code=source_code.split("#NEXT")
            for block in source_code:
                    if block.startswith("\n#"+word[0]):
                        return block


with open("program.Eso") as file:
    code = file.read()
    print(code)
    print('---------------------')
    compiler = EsoFurCompiler()
    compiler.compile(code)