from itertools import tee


def pairwise(iterable):  # itertools pairwise, added in 3.10 (I am using 3.9)
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def predict_next(sequence):
    def get_difference(sequence):
        return [b - a for a, b in pairwise(sequence)]

    if not any(sequence):  # base case - all 0s
        return 0
    
    return predict_next(get_difference(sequence)) + sequence[-1]


def predict_previous(sequence):
    def get_difference(sequence):
        return [b - a for a, b in pairwise(sequence)]
    
    if not any(sequence):  # base case - all 0s
        return 0
    
    return sequence[0] - predict_previous(get_difference(sequence))


def main():
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
    
    # Part 1
    predicted_values = []
    for line in lines:
        sequence = [int(v) for v in line.split()]
        predicted_values.append(predict_next(sequence))

    total = sum(predicted_values)
    print(total)

    # Part 2
    predicted_values = []
    for line in lines:
        sequence = [int(v) for v in line.split()]
        predicted_values.append(predict_previous(sequence))

    total = sum(predicted_values)
    print(total)

main()
