def extract_digits_from_string(string: str):
    result = ''
    for letter in string:
        if letter.isdigit():
            result += letter
    
    if len(result) >= 2:
        to_return = result[0] + result[-1]
        return int(to_return)
    
    to_return = int(result * 2)
    return to_return


total = 0

while True:
    line = input()
    if line == '':
        break
    total += extract_digits_from_string(line)

print(total)