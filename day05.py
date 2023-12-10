import re
from typing import Optional


def batched(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

class ProductionMap:
    def __init__(self, ranges: list[tuple[int, int, int]]):
        self._ranges = ranges

    def get(self, val: int) -> int:
        for destination, source, range_ in self._ranges:
            if source <= val < source + range_:
                return destination + (val - source)
        
        
        return val

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self._ranges})'


def parse_map_ints(line, pattern=r'(\d+)\D+(\d+)\D+(\d+)') -> Optional[tuple[int, int, int]]:
    match = re.match(pattern, line)

    if match:
        return int(match.group(1)), int(match.group(2)), int(match.group(3))


def parse_input(lines):
    seeds = [int(num) for num in re.findall(r'\d+', lines[0])]
    
    maps = []
    current_map = []
    for result in (parse_map_ints(line) for line in lines[2:]):
        if result:
            current_map.append(result)
        else:
            maps.append(current_map)
            current_map = []
    
    maps.append(current_map)
    production_maps = [ProductionMap(map_) for map_ in filter(None, maps)]
    return seeds, production_maps


def main():
    with open('input', 'r') as fp:
        lines = [line.strip() for line in fp]

    seeds, maps = parse_input(lines)
    for production_map in maps:
        seeds = [production_map.get(seed) for seed in seeds]

    lowest = min(seeds)
    print(lowest)

    # Part 2
    # didn't figure out optimization so haven't completed part 2 yet
    _, maps = parse_input(lines)
    seeds = batched(lines[0].removeprefix('seeds: ').split(), 2)

    lowest = float('inf')
    for start, range_ in seeds:
        start, range_ = int(start), int(range_)
        for num in range(start, start+range_):
            for production_map in maps:
                num = production_map.get(num)
            lowest = min(lowest, num)
    
    print(lowest)




main()

