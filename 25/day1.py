with open("day1_input.txt") as f:
    lines = f.readlines()

with open("day1_testinput.txt") as f:
    testlines = f.readlines()

def part1():
    position = 50
    zeroes = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:].strip())

        if direction == 'L':
            position -= distance % 100
        elif direction == 'R':
            position += distance % 100
        
        position %= 100
        if position < 0:
            position += 100
        
        print(f"Current position: {position}")
        if position == 0:
            zeroes += 1
    
    print(f"Total times at position 0: {zeroes}")

def part2():
    postion = 50
    zeroes = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:].strip())

        full_loops = distance // 100
        zeroes += full_loops
        partial_loop = distance % 100

        relative_pos = postion + partial_loop if direction == 'R' else postion - partial_loop
        if (relative_pos <= 0 and postion != 0) or relative_pos > 99:
            zeroes += 1
            print("passed zero")

        postion = relative_pos % 100
        print(f"postion: {postion}")
    
    print(f"passed zero {zeroes} times")



if __name__ == "__main__":
    part2()


    