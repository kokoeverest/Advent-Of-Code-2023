numbers_dict = {
    "1": 1, "one": 1,
    "2": 2, "two": 2,
    "3": 3, "three": 3,
    "4": 4, "four": 4,
    "5": 5, "five": 5,
    "6": 6, "six": 6,
    "7": 7, "seven": 7,
    "8": 8, "eight": 8,
    "9": 9, "nine": 9
    }

def extract_digits_from_string(string: str):
    original_string = string[::-1]
    result1 = ''
    result2 = ''

    while True:
        if string == '': 
            break

        for symbol in numbers_dict:
            if string.startswith(symbol):
                result1 += str(numbers_dict[symbol])
                string = string.replace(symbol, '', 1)
                break
        else:
            string = string[1:]
        
    while True:
        if original_string == '': 
            break

        for symbol in numbers_dict:
            if original_string.startswith(symbol[::-1]):
                result2 += str(numbers_dict[symbol])
                original_string = original_string.replace(symbol[::-1], '', 1)
                break
        else:
            original_string = original_string[1:]

    if len(result1) >= 2:
        to_return = result1[0] + result2[0]
        return int(to_return)
    
    to_return = int(result1 * 2)
    return to_return


total = 0

while True:
    line = input()
    if line == '':
        break
    total += extract_digits_from_string(line)

print(total)