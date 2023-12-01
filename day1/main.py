from typing import Callable

""" part one """
def get_first_digit(s: str) -> str:
    for char in s:
        if char.isdigit():
            return char
    
    return "0"

with open('calibration', 'r') as fp:
    total = sum(int(get_first_digit(line) + get_first_digit(reversed(line))) for line in fp)

print(total)


""" part two """
from trie import Trie

numbers_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
numbers_mapping_backwards = {k[::-1]: v for k, v in numbers_mapping.items()}

trie_forwards = Trie(numbers_mapping.keys())
trie_backwards = Trie(numbers_mapping_backwards.keys())

def get_first_digit_v2(s: str, get_first_word: Callable, numbers_mapping: dict[str, int]) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        
        word = get_first_word(s[i:])
        if word:
            return numbers_mapping[word]

    return "0"


with open('calibration', 'r') as fp:
    total = 0
    for calibration_value in fp:
        left = get_first_digit_v2(calibration_value, trie_forwards.get_first_word, numbers_mapping)
        right = get_first_digit_v2(calibration_value[::-1], trie_backwards.get_first_word, numbers_mapping_backwards)
        total += int(left + right)

print(total)
