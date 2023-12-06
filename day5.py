#AoC Day 5 Day 5: If You Give A Seed A Fertilizer

seeds, *maps = open("input_day5.txt").read().split('\n\n')
seeds = [int(seed) for seed in seeds.split()[1:]]
maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]


original_locations = seeds
for map in maps:
    transformed_locations = []
    for original_location in original_locations:
        new_location = original_location
        for destination, start, size in map:
            if start <= original_location < start + size:
                new_location = original_location - start + destination
                break
        transformed_locations.append(new_location)
    original_locations = transformed_locations

print(min(original_locations))