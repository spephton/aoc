
def main():
    with open('input5.txt') as fp:
        puzzle_input = fp.readlines()

    parsing_cursor = 0

    seeds = {int(seedno.strip()) for seedno in puzzle_input[parsing_cursor].split(':')[1].split()}

    print(f'seeds: {seeds}')

    parsing_cursor += 3

    maps = []

    while parsing_cursor < len(puzzle_input):
        current_map = []
        while parsing_cursor < len(puzzle_input) and is_num(puzzle_input[parsing_cursor][0]):
            numstrings = puzzle_input[parsing_cursor].strip().split()
            current_map.append([int(number.strip()) for number in numstrings])
            parsing_cursor += 1
        maps.append(current_map)
        parsing_cursor += 2

    categories = ["soils", "fertilizers", "waters", "lights", "temperatures", "humidities", "locations"]


    elements_of_category = seeds
    for category, category_map in zip(categories, maps):
        elements_of_category = propagate(elements_of_category, category_map)
        print(f"{category}: {elements_of_category}")

    print(f'Minumum location: {min(elements_of_category)}')

class BijectionError(Exception):
    pass

def propagate(elements, category_map):
    new_elements = set()
    for map_range in category_map:
        if len(elements) == 0:
            break
        dest_range_start, src_range_start, range_len = map_range

        elements_to_remove = []
        for element in elements:
            if element >= src_range_start and element < src_range_start + range_len:
                elements_to_remove.append(element)
                shifted_element = element + (dest_range_start - src_range_start)
                if shifted_element in new_elements:
                    raise BijectionError(f'Collision when mapping element {element} to {shifted_element}')
                new_elements.add(shifted_element)

        for element in elements_to_remove:
            elements.remove(element)
    for element in elements:
        if element in new_elements:
            raise BijectionError(f'Collision when mapping element {element} to itself')
        new_elements.add(element)
    return new_elements




def is_num(char):
    try:
        int(char)
    except ValueError:
        return False
    return True

if __name__ == "__main__":
    main()
