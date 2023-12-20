def check_surroundings(row, col):
    directions = [look_left, look_right, look_up, look_down]
    symbols = []
    for direction in directions:
        symbols.extend(direction(row, col))
    if len(symbols) > 0:
        return True
    return False

def look_left(row, col):
    left_symbols = []
    if col > 0:
        if matrix[row][col-1] != '.' and not matrix[row][col-1].isdigit() and matrix[row][col-1] != "N":
            left_symbols.append(matrix[row][col-1])
    return left_symbols

def look_right(row, col):
    right_symbols = []
    if col + 1 < len(matrix[row]):
        if matrix[row][col+1] != '.' and not matrix[row][col+1].isdigit() and matrix[row][col+1] != "N":
            right_symbols.append(matrix[row][col+1])
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
            if matrix[row-1][i] != '.' and not matrix[row-1][i].isdigit() and matrix[row-1][i] != "N":
                upper_symbols.append(matrix[row-1][i])
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
            if matrix[row+1][i] != '.' and not matrix[row+1][i].isdigit() and matrix[row+1][i] != "N":
                lower_symbols.append(matrix[row+1][i])
    return lower_symbols
            

matrix: list[str] = []
result_sum = 0

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
        if matrix[row][symbol].isdigit():
            temp_num += matrix[row][symbol]
            temp_num_coordinates.append((row, symbol))
        else:
            if temp_num == "":
                continue
            else:
                for position in temp_num_coordinates:
                    r, c = position
                    part_number = check_surroundings(r, c)
                    if part_number: 
                        result_sum += int(temp_num)
                        break
                temp_num = ""
                temp_num_coordinates = []
                part_number = False

print(result_sum)