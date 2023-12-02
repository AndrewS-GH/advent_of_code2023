from functools import reduce
import operator


def parse_game(line: str) -> tuple[int, list[list[tuple[int, str]]]]:
    id, game_str = line.split(':')
    id = int(id.split()[-1])

    game_str = game_str.replace(',', ';')
    game = [(int(num), color) for num, color in (roll.split() for roll in game_str.split(';'))]

    return id, game


def main():
    with open("input") as fp:
        lines = fp.readlines()
    
    # part 1
    max_colors = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for line in lines:
        id, game = parse_game(line)
        for num, color in game:
            if num > max_colors[color]:
                break
        else:
            total += id
    
    print(total)

    # part 2
    total = 0
    for line in lines:
        id, game = parse_game(line)
        max_colors = {}
        for num, color in game:
            if color not in max_colors:
                max_colors[color] = num
                continue

            max_colors[color] = max(max_colors[color], num)
        total += reduce(operator.mul, max_colors.values())
    
    print(total)

if __name__ == "__main__":
    main()
