with open('input4.txt') as fp:
    puzzle_input = fp.readlines()

copies = [1 for line in puzzle_input]
for game_number, line in enumerate(puzzle_input):
    numbers = line.split(':')[1].strip()
    winning_numbers_string, game_numbers_string = numbers.split('|')

    winning_number_strings = winning_numbers_string.split()
    winning_numbers = {int(number_string.strip()) for number_string in winning_number_strings}
    
    game_number_strings = game_numbers_string.split()
    game_numbers = {int(number_string.strip()) for number_string in game_number_strings}

    in_both = winning_numbers.intersection(game_numbers)

    number_won = len(in_both)

    for subsequent_game_number in range(game_number + 1, game_number + 1 + number_won):
        copies[subsequent_game_number] += copies[game_number]

print(sum(copies))


