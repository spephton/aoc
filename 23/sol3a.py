with open('input3.txt') as fp:
    puzzle_input = fp.readlines()

def is_number(a_string):
    try:
        int(a_string)
    except ValueError:
        return False
    return True

def is_symbol(a_char):
    if is_number(a_char) or a_char == '.' or a_char == '\n':
        return False
    return True

col_cursor = -1
row_cursor = 0

part_numbers = []

while True:
    col_cursor += 1
    if col_cursor >= len(puzzle_input[row_cursor]):
        col_cursor = 0
        row_cursor += 1

    if row_cursor >= len(puzzle_input):
        break


    if not is_number(puzzle_input[row_cursor][col_cursor]):
        continue

    # How long is this number?
    end_col = col_cursor + 1
    while end_col < len(puzzle_input[row_cursor]) - 1 and is_number(puzzle_input[row_cursor][end_col]):
        end_col += 1


    # Part number is only valid if we can find a symbol adjacent (even diagonally)
    # Symbols are any char except a number or '.'
    valid_part_number = False
    if col_cursor > 0 and is_symbol(puzzle_input[row_cursor][col_cursor - 1]):
        valid_part_number= True
    elif is_symbol(puzzle_input[row_cursor][end_col]):
        valid_part_number= True
    else:
        start_scan_col = col_cursor - 1 if col_cursor > 0 else col_cursor
        end_scan_col = end_col + 1
        if row_cursor > 0:
            for col in range(start_scan_col, end_scan_col):
                if is_symbol(puzzle_input[row_cursor - 1][col]):
                    valid_part_number = True
        if row_cursor < len(puzzle_input) - 1:
            for col in range(start_scan_col, end_scan_col):
                if is_symbol(puzzle_input[row_cursor + 1][col]):
                    valid_part_number = True


            

    if valid_part_number:
        print(puzzle_input[row_cursor][col_cursor:end_col])
        part_numbers.append(int(puzzle_input[row_cursor][col_cursor:end_col]))

    col_cursor = end_col - 1

print(sum(part_numbers))



    




