with open("input2.txt") as fp:
    lines = fp.readlines()

sum_powers = 0
for line in lines:
    red_max = 0
    green_max = 0
    blue_max = 0
    
    line = line.strip()
    semicolon_loc = line.find(":")

    game_id_str = line[5:semicolon_loc]
    game_id = int(game_id_str)

    game_data = line[semicolon_loc + 2:]

    sets = game_data.split(';')
    for set in sets:
        for qty_color in set.split(','):
            str_qty, color = qty_color.strip().split()
            qty = int(str_qty)
            
            if color == 'red' and qty > red_max:
                red_max = qty
            elif color == 'green' and qty > green_max:
                green_max = qty
            elif color == 'blue' and qty > blue_max:
                blue_max = qty
            

    game_power = red_max * green_max * blue_max
    sum_powers += game_power
    

print(sum_powers)



