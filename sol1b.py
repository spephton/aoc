calibration_values = []

with open('input1.txt') as fp:
    lines = fp.readlines()

acc = 0
for line_number, line in enumerate(lines):
    first = None
    last = None

    digitstrings = [
        'zero',
        'one',
        'two',
        'three',
        'four', 
        'five', 
        'six',
        'seven',
        'eight',
        'nine',
    ]
    


    index_first_occurrence = -1
    value_first_occurrence = -1
    index_last_occurrence = -1
    value_last_occurrence = -1



    for n, digitstring in enumerate(digitstrings):
        first_occurrence_thisdigit = line.find(digitstring)
        digitfound = first_occurrence_thisdigit >= 0
        if digitfound:
            if index_first_occurrence == -1 or first_occurrence_thisdigit < index_first_occurrence:
                index_first_occurrence = first_occurrence_thisdigit
                value_first_occurrence = n

        last_occurrence_thisdigit = line.rfind(digitstring)
        if last_occurrence_thisdigit > index_last_occurrence:
            index_last_occurrence = last_occurrence_thisdigit
            value_last_occurrence = n

    print(f'line {line_number}: first stringdigit: {value_first_occurrence}, last stringdigit: {value_last_occurrence}')

    first_intchar_index = None
    first_intchar_value = None
    last_intchar_index = None
    last_intchar_value = None

    for n, character in enumerate(line):
        try:
            thisvalue = int(character)
        except ValueError:
            continue

        if first_intchar_index is None:
            first_intchar_index = n
            first_intchar_value = thisvalue

        last_intchar_index = n
        last_intchar_value = thisvalue

    print(f"{first_intchar_value}{last_intchar_value}")

    first_int = None
    last_int = None
    
    if index_first_occurrence == -1 or first_intchar_index < index_first_occurrence:
        # assume that there is always a valid intchar
        first_int = first_intchar_value
    else:
        first_int = value_first_occurrence

    if index_last_occurrence == -1 or last_intchar_index > index_last_occurrence:
        # assume that there is always a valid intchar
        last_int = last_intchar_value
    else:
        last_int = value_last_occurrence
    
    print(f"first int: {first_int}, last int {last_int}")
    calibration_value = first_int * 10 + last_int
    acc += calibration_value

print(acc)






'''
    if first is None:
        raise ValueError(f'Invalid input (line {line_number} does not contain any integers)')

    if last is None:
        last = first

    print(f'line number {line_number}')
    this_calibration_value = 10 * first + last

    calibration_values.append(this_calibration_value)

print(sum(calibration_values))
'''
