""" part one """
def get_first_digit(s: str) -> str:
    for char in s:
        if char.isdigit():
            return char
    
    return "0"

with open('calibration', 'r') as fp:
    total = sum(int(get_first_digit(line) + 
get_first_digit(reversed(line))) for line in fp)

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
numbers_mapping_backwards = {k[::-1]: v for k, v in 
numbers_mapping.items()}

trie_forwards = Trie(numbers_mapping.keys())
trie_backwards = Trie(numbers_mapping_backwards.keys())

shortest_word = len(min(numbers_mapping, key=len))


def get_first_digit_v2(s: str, trie: Trie, numbers_mapping: dict[str, 
int], shortest_word: int = 1) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        
        for j in range(i+shortest_word, len(s)):
            phrase = s[i:j]
            is_word, is_prefix = trie.search(phrase)
            if is_word:
                return numbers_mapping[phrase]
            if not is_prefix:
                break
    return "0"


with open('calibration', 'r') as fp:
    total = 0
    for calibration_value in fp:
        left = get_first_digit_v2(calibration_value, trie_forwards, 
numbers_mapping, shortest_word)
        right = get_first_digit_v2(calibration_value[::-1], 
trie_backwards, numbers_mapping_backwards, shortest_word)
        total += int(left + right)

print(total)

