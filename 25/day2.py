testinput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
with open("day2_input.txt") as f:
    realinput = f.readlines()[0].strip()

def part1():
    ranges = realinput.split(",")
    acc = 0

    for some_range in ranges:
        lower_str, upper_str = some_range.split("-")
        lower = int(lower_str)
        upper = int(upper_str)

        print(f"Considering {lower} to {upper}")
        for i in range(lower, upper + 1):
            digits = str(i)
            if len(digits) % 2 != 0:
                # cannot be a sequence repeated twice if there are an odd number of digits
                continue
            middle = len(digits)//2
            if digits[:middle] == digits[middle:]:
                print(f"{digits} is invalid")
                acc += i

    print(f"sum of invalid: {acc}")

def part2():
    ranges = realinput.split(",")
    acc = 0

    for some_range in ranges:
        lower_str, upper_str = some_range.split("-")
        lower = int(lower_str)
        upper = int(upper_str)

        print(f"Considering {lower} to {upper}")
        for i in range(lower, upper + 1):
            digits = str(i)
            for n in range(1, len(digits)):
                if len(digits) % n != 0:
                    # this n does not divide the digits into even groups
                    continue
                first_group = digits[:n]
                end_of_group = n + n
                failed = False
                while end_of_group <= len(digits):
                    if digits[end_of_group-n:end_of_group] != first_group:
                        failed = True
                        break
                    end_of_group += n
                if not failed:
                    print(f"{digits} is invalid")
                    acc += i
                    break

    print(f"sum of invalid: {acc}")

if __name__ == "__main__":
    part2()
    