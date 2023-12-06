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

gear_ratios = []

while True:
    col_cursor += 1
    if col_cursor >= len(puzzle_input[row_cursor]):
        col_cursor = 0
        row_cursor += 1

    if row_cursor >= len(puzzle_input):
        break


    if not puzzle_input[row_cursor][col_cursor] == '*':
        continue

    print(f'asterisk at ({row_cursor}, {col_cursor})')

    # There are 8 positions around the '*' that could contain a digit
    # For left and right it's simple -- if there's a digit there, there's a number there
    # For the top (including corners) and bottom (ditto), if there is a number directly down or up from 
    # the '*' then there is one number there. Only if both sides have a number and the center does not
    # can we have two numbers in one row

    # If we can find exactly two numbers adjacent to a '*' then that '*' is a gear

    num_positions = []

    # Top
    if row_cursor > 0:
        if is_number(puzzle_input[row_cursor - 1][col_cursor]):
            num_positions.append((-1,0))
            print('found up')
        else:
            if col_cursor > 0 and is_number(puzzle_input[row_cursor - 1][col_cursor - 1]):
                num_positions.append((-1, -1))
                print('found up left')
            if is_number(puzzle_input[row_cursor - 1][col_cursor + 1]):
                num_positions.append((-1, 1))
                print('found up right')

    # Bottom
    if row_cursor < len(puzzle_input) - 1:
        if is_number(puzzle_input[row_cursor + 1][col_cursor]):
            num_positions.append((1, 0))
            print('found down')
        else:
            if col_cursor > 0 and is_number(puzzle_input[row_cursor + 1][col_cursor - 1]):
                num_positions.append((1, -1))
                print('found down left')
            if is_number(puzzle_input[row_cursor + 1][col_cursor + 1]):
                num_positions.append((1, 1))
                print('found down right')
            
    # Sides
    if col_cursor > 0 and is_number(puzzle_input[row_cursor][col_cursor - 1]):
        num_positions.append((0, -1))
        print('found left')
    if is_number(puzzle_input[row_cursor][col_cursor + 1]):
        num_positions.append((0, 1))
        print('found right')

    if len(num_positions) != 2:
        continue
    

    gear_ratio_factors =[]
    for row_offset, column_offset in num_positions:
        num_row = row_cursor + row_offset
        start_num_col = col_cursor + column_offset
        end_num_col = col_cursor + column_offset
        while start_num_col >= 0 and is_number(puzzle_input[num_row][start_num_col]):
            start_num_col -= 1
        while is_number(puzzle_input[num_row][end_num_col]):
            end_num_col += 1
        start_num_col += 1

        gear_ratio_factors.append(int(puzzle_input[num_row][start_num_col:end_num_col]))

    assert len(gear_ratio_factors) == 2

    print(gear_ratio_factors[0])
    print(gear_ratio_factors[1])
    gear_ratio = gear_ratio_factors[0] * gear_ratio_factors[1]
    print(gear_ratio)
    gear_ratios.append(gear_ratio)





            



print(sum(gear_ratios))



    




