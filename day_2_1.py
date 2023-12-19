def cube_counter(sets: list[str]) -> bool:
    for s in sets:
        s = s.split(", ")
        for g in s:
            count, color = g.split()
            if int(count) > cubes[color]:
                return False
    return True

def line_splitter(line: str):
    game_id, sets = line.split(": ")
    game_id = game_id.split()
    sets = sets.split("; ")    
    return int(game_id[1]), sets

id_sum = 0
cubes = {"blue": 14, "green": 13, "red": 12}

while True:
    line = input()
    if line == '':
        break
    game_id, sets = line_splitter(line)
    possible_game = cube_counter(sets)

    if possible_game:
        id_sum += game_id

print(id_sum)