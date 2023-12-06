# let's build a lexer-pattern solution to this one.

with open('input3a.txt') as fp:
    data_lines = fp.readlines()

class InputReader():

    def __init__(self, data_lines):
        self.data_lines = data_lines

    line_no = 0
    col_no = -1

    def nextchar(self):
        self.col_no += 1
        if self.col_no >= len(self.data_lines[self.line_no]):
            self.col_no = 0
            self.line_no += 1
        if self.line_no >= len(self.data_lines):
            self.line_no = 0
            self.col_no = -1
            return None

        return self.data_lines[self.line_no][self.col_no]

    def peek(self, n=1):
        n_remain = n
        current_col = self.col_no + 1
        current_line = self.line_no
        buf = ''
        while n_remain > 0:
            n_from_current_line = len(self.data_lines[current_line]) - current_col
            if n_remain <= n_from_current_line:
                buf += self.data_lines[current_line][current_col : current_col + n_remain]
                return buf
            n_remain -= n_from_current_line
            buf += self.data_lines[current_line][current_col : current_col + n_from_current_line]
            current_line += 1
            if current_line >= len(self.data_lines):
                return buf
        return buf

def is_number(inputstring):
    try:
        int(inputstring)
    except ValueError:
        return False
    return True

ireader = InputReader(data_lines)

part_numbers = []
symbol_seen = False
number_buffer = ''
while True:
    current_char = ireader.nextchar()
    if current_char is None:
        if len(number_buffer) > 0 and symbol_seen:
            part_numbers.append(int(number_buffer))
        break

    if current_char is '.':
        if len(number_buffer) > 0 and symbol_seen:
            part_numbers.append(int(number_buffer))
        number_buffer = ''
        symbol_seen = False
        continue
    
    if is_number(current_char):
        number_buffer += current_char
        continue

    # considering every other character that is not a .... oh god I misread the bloody question lol
    # let's start again.
