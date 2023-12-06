RED_TOTAL = 12
GREEN_TOTAL = 13
BLUE_TOTAL = 14


with open("input2.txt") as fp:
    lines = fp.readlines()

sum_possible_game_ids = 0
for line in lines:
    game_found_invalid = False
    
    line = line.strip()
    semicolon_loc = line.find(":")

    game_id_str = line[5:semicolon_loc]
    game_id = int(game_id_str)

    game_data = line[semicolon_loc + 2:]

    sets = game_data.split(';')
    for set in sets:
        for qty_color in set.split(','):
            qty, color = qty_color.strip().split()
            
            is_invalid_set = (
                    (color == 'red' and int(qty) > RED_TOTAL) or
                    (color == 'green' and int(qty) > GREEN_TOTAL) or
                    (color == 'blue' and int(qty) > BLUE_TOTAL)
            )
            if is_invalid_set:
                game_found_invalid = True

    if game_found_invalid:
        print(game_id)
    else:
        sum_possible_game_ids += game_id

print(sum_possible_game_ids)



