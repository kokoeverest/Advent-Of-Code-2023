def check_surroundings(row, col):
    directions = [look_left, look_right, look_up, look_down]
    symbols: list[tuple[int]] = []
    for direction in directions:
        symbols.extend(direction(row, col))
    if len(symbols) > 0:
        return True, next((s for s in symbols), [])
    return False, symbols

def look_left(row, col):
    left_symbols = []
    if col > 0:
        symbol = matrix[row][col-1]
        if symbol != '.' and not symbol.isdigit() and symbol != "N":
            left_symbols.append((row, col-1))
    return left_symbols

def look_right(row, col):
    right_symbols = []
    if col + 1 < len(matrix[row]):
        symbol = matrix[row][col+1]
        if symbol != '.' and not symbol.isdigit() and symbol != "N":
            right_symbols.append((row, col+1))
    return right_symbols

def look_up(row: int, col: int):
    upper_symbols = []
    if col == 0:
        ran = (col, col+1)
    elif col == len(matrix[row]) - 1:
        ran = (col-1, col)
    else:
        ran = (col-1, col, col+1)
    if row-1 >= 0:
        for i in ran:
            symbol = matrix[row-1][i]
            if symbol != '.' and not symbol.isdigit() and symbol != "N":
                upper_symbols.append((row-1, i))
    return upper_symbols

def look_down(row, col):
    lower_symbols = []
    if col == 0:
        ran = (col, col+1)
    elif col == len(matrix[row]) - 1:
        ran = (col-1, col)
    else:
        ran = (col-1, col, col+1)
    if row+1 < len(matrix):
        for i in ran:
            symbol = matrix[row+1][i]
            if symbol != '.' and not symbol.isdigit() and symbol != "N":
                lower_symbols.append((row+1, i))
    return lower_symbols
            

matrix: list[str] = []
result_sum = 0
gears = {}
gear_ratio = ''

while True:
    line = input()
    if line == '':
        break
    matrix.append(f"{line}N")

for row in range(len(matrix)):
    temp_num = ""
    temp_num_coordinates: list[tuple[int, int]] = []
    part_number = False
    for symbol in range(len(matrix[row])):
        if matrix[row][symbol] == "*":
            if (row, symbol) not in gears: gears[(row, symbol)] = []
        if matrix[row][symbol].isdigit():
            temp_num += matrix[row][symbol]
            temp_num_coordinates.append((row, symbol))
        else:
            
            if temp_num == "":
                continue
            else:
                for position in temp_num_coordinates:
                    r, c = position
                    part_number, sym = check_surroundings(r, c)
                    if part_number:
                        if sym not in gears:
                            gears[sym] = []
                        gears[sym].append(temp_num_coordinates)
                        break
                temp_num = ""
                temp_num_coordinates = []
                part_number = False

for key, value in gears.items():
    r,c = key
    s = matrix[r][c]
    if s == "*" and len(value) == 2:
        temp_num = ''
        for i in value:
            for t in i:
                temp_num += matrix[t[0]][t[1]]
            temp_num += "*"
        result_sum += eval(temp_num.removesuffix("*"))
        
print(result_sum)