with open('input4.txt') as fp:
    puzzle_input = fp.readlines()

total_score = 0
for line in puzzle_input:
    numbers = line.split(':')[1].strip()
    winning_numbers_string, game_numbers_string = numbers.split('|')

    winning_number_strings = winning_numbers_string.split()
    winning_numbers = {int(number_string.strip()) for number_string in winning_number_strings}
    
    game_number_strings = game_numbers_string.split()
    game_numbers = {int(number_string.strip()) for number_string in game_number_strings}

    in_both = winning_numbers.intersection(game_numbers)

    number_won = len(in_both)

    if number_won > 0:
        game_score = 2 ** (number_won - 1)
        total_score += game_score

print(total_score)

