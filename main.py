class EsoFurCompiler:
    def __init__(self):
        self.symbol_table = {}
        self._in_comment = False

    def compile(self, code):
        lines = code.split('\n')
        i = 0
        built=False
        while i < len(lines):
            line = lines[i].strip()

            # Skip empty lines
            if not line:
                i+=1
                continue

            if "OwO What's This?" in line :
              built=True
              i+=1
              continue

            elif not built:
              exit(0)

            if line=="QwQ":
              exit("finished")

            if "QwQ" not in lines:
              exit(1)

            # Comment handling
            if line.startswith('Muzzles'):
                i+=1
                continue

            # Variable declaration
            if line.startswith('Notices Your'):
                var_name = line.split(' ')[2]
                self.symbol_table[var_name] = None
                i+=1
                continue

            # Assignment
            if 'Pounces On' in line:
                value, var_name = line.split('Pounces On')
                var_name = var_name.strip()
                value = self._parse_value(value.strip())
                self.symbol_table[var_name] = value
                i+=1
                continue

            # Jumps
            if 'Nuzzles' in line:
                condition, label = line.split('Nuzzles')
                condition = self._parse_value(condition.strip())  # evaluate condition
                label = label.strip()
                if bool(condition):  # use bool() to convert the parsed condition to aboolean
                  i = int(self._find_label_index(lines, label))
                else:
                 i+=1
                continue


            # Loops
            if line == '*Starts Roleplaying*':
                i+=1
                continue

            if line.startswith('*Stops Roleplaying'):
                condition = line.split(' ')[-1]
                condition = self._parse_value(condition)
                if condition > 0:
                    i = self._find_loop_start_index(lines, i)
                else:
                  i+=1
                continue

            # Print
            if line.startswith('Howl'):
                var_name = line.split(' ')[-1]
                value = self._parse_value(var_name)
                print(value)
                i+=1
                continue

              # Ask user for input
            if line.startswith('Boop The User For'):
              var_name = line.split(' ')[-1]
              value = input()
              self.symbol_table[var_name] = value
              i+=1
              continue


            # Type casting
            if 'Transforms Into' in line:
                var_name, type_name = line.split('Transforms Into ')
                var_name = var_name.strip()
                type_name = type_name.strip()
                value = self._parse_value(var_name)
                self.symbol_table[var_name] = self._cast_value(value, type_name)
                i+=1
                continue

        # Check for unclosed multiline comments
        #if self._in_comment:
        #    print("Error: Unclosed multiline comment!")

    def _find_label_index(self, lines, label):
        if label.isdigit():
          return label
        for i, line in enumerate(lines):
            if line.startswith('Marks') and line.split(' ')[1] == label:
                return i
        print(f"Error: Label not found: {label}")

    def _find_loop_start_index(self, lines, end_index):
        for i in range(end_index - 1, -1, -1):
            if lines[i] == '*Starts Roleplaying*':
                return i
        print("Error: Loop start not found")

    def _parse_value(self, value_str):
        if value_str.isdigit():
            return int(value_str)
        if value_str in self.symbol_table:
            return self.symbol_table[value_str]
        try:
            return eval(value_str, {}, self.symbol_table)
        except:
            print(f"Error: Invalid expression: {value_str}")


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
        print(f"Error: Invalid type: {type_name}")




code='''
OwO What's This?
Notices Your Input
Howl "INPUT"
Boop The User For Input
Input Transforms Into Int
Input Nuzzles 8
Howl 0
Nuzzles 7
Howl "LOOP"
*Starts Roleplaying*
Howl 1
*Stops Roleplaying Because Of Input*
Howl "STOP"
QwQ
'''

compiler = EsoFurCompiler()
compiler.compile(code)
