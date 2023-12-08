import re
from functools import reduce
import operator

get_ints_pattern = r'\b\d+\b'


def valid_wait_time(time, distance, wait_time):
    # wait time = speed
    time -= wait_time
    return (wait_time * time) > distance


def main():
    # Part 1
    with open('input', 'r') as fp:
        times = [int(v) for v in re.findall(get_ints_pattern, fp.readline())]
        distances = [int(v) for v in re.findall(get_ints_pattern, fp.readline())]

    wins = []
    for time, distance in zip(times, distances):
        total_wins = sum(valid_wait_time(time, distance, i) for i in range(1, time))
        wins.append(total_wins)

    result = reduce(operator.mul, wins)
    print(result)

    # Part 2
    # maybe later I will come back and figure out the optimal algorithm (probably not)
    with open('input', 'r') as fp:
        time = int("".join(re.findall(get_ints_pattern, fp.readline())))
        distance = int("".join(re.findall(get_ints_pattern, fp.readline())))

    total_wins = sum(valid_wait_time(time, distance, i) for i in range(1, time))
    print(total_wins)


main()
