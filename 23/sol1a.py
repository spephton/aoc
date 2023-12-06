calibration_values = []

with open('input1.txt') as fp:
    lines = fp.readlines()

for line_number, line in enumerate(lines):
    first = None
    last = None
    for character in line:
        try:
            an_integer = int(character)
        except ValueError:
            continue
        if first == None:
            first = an_integer
        else:
            last = an_integer

    if first is None:
        raise ValueError(f'Invalid input (line {line_number} does not contain any integers)')

    if last is None:
        last = first

    print(f'line number {line_number}')
    this_calibration_value = 10 * first + last

    calibration_values.append(this_calibration_value)

print(sum(calibration_values))
