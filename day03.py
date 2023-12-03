from itertools import product
from collections import defaultdict


class EnginePart:
    def __init__(self, digits: list[str], positions: list[tuple[int, int]]) -> None:
        self._digits = digits
        self._positions = positions
        self._neighbors = None

    @property
    def neighbors(self):
        if not self._neighbors:
            all_neighbors = []
            for r, c in self._positions:
                for r_add, c_add in product([-1, 0, 1], repeat=2):
                    all_neighbors.append((r+r_add, c+c_add))
            
            self._neighbors = set(all_neighbors) - set(self._positions)
        
        return self._neighbors
                
    @property
    def value(self):
        return int("".join(self._digits))
    
    def __repr__(self) -> str:
        return "{}({}, {})".format(type(self).__name__, self._digits, self._positions)


def get_engine_parts(lines):
    engine_parts = []
    rows, cols = len(lines), len(lines[0])
    for row in range(rows):
        col = 0
        while col < cols:
            if not lines[row][col].isdigit():
                col += 1
                continue
            
            digits, positions = [], []
            while col < cols and lines[row][col].isdigit():
                digits.append(lines[row][col])
                positions.append((row, col))
                col += 1
            
            engine_parts.append(EnginePart(digits, positions))
    
    return engine_parts


def get_symbols(lines):
    positions = []
    rows, cols = len(lines), len(lines[0])
    for row in range(rows):
        for col in range(cols):
            if not lines[row][col].isdigit() and lines[row][col] != ".":
                positions.append((row, col))
    return positions


def get_gears(lines):
    positions = []
    rows, cols = len(lines), len(lines[0])
    for row in range(rows):
        for col in range(cols):
            if lines[row][col] == "*":
                positions.append((row, col))

    return positions


def main():
    with open("input", "r") as f:
        lines = [line.strip() for line in f]
    
    # part 1
    engine_parts: list[EnginePart] = get_engine_parts(lines)
    symbols: set[tuple[int, int]] = set(get_symbols(lines))
    
    
    valid_engine_parts = []
    for engine_part in engine_parts:
        if engine_part.neighbors & symbols:
            valid_engine_parts.append(engine_part)
        
    total = sum(part.value for part in valid_engine_parts)
    print(total)

    # part 2
    engine_parts: list[EnginePart] = get_engine_parts(lines)
    gears: set[tuple[int, int]] = set(get_gears(lines))
    
    gear_to_parts = defaultdict(list)
    for engine_part in engine_parts:
        for position in engine_part.neighbors & gears:
            gear_to_parts[position].append(engine_part)

    total = sum(parts[0].value * parts[1].value for parts in gear_to_parts.values() if len(parts) == 2)
    print(total)


main()
