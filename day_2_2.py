def power_calculator(sets: list[str]) -> int:
    cubes = {"blue": [], "green": [], "red": []}
    for s in sets:
        s = s.split(", ")
        for g in s:
            count, color = g.split()
            cubes[color].append(int(count))
    
    power = max(cubes["blue"])
    for k, v in cubes.items():
        if k != "blue": power *= max(v)   
    return power

def line_splitter(line: str):
    game_id, sets = line.split(": ")
    game_id = game_id.split()
    sets = sets.split("; ")    
    return int(game_id[1]), sets

sum_powers = 0

while True:
    line = input()
    if line == '':
        break
    game_id, sets = line_splitter(line)
    sum_powers += power_calculator(sets)

print(sum_powers)