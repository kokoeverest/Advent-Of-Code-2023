def line_splitter(line: str):
    card_id, numbers = line.split(": ")
    card_id = card_id.strip().split()
    numbers = numbers.strip().split("|")    
    return int(card_id[1]), numbers

def calculate_price(count: int):
    if count == 1: 
        return 1
    elif count > 1: 
        return 2

price = 0

while True:
    line = input()
    if line == '':
        break
    card_id, numbers = line_splitter(line)
    winning_numbers = set(map(int, numbers[0].split()))
    other_numbers = set(map(int, numbers[1].split()))
    matches = winning_numbers.intersection(other_numbers)
    card_price = 0
    for count, match in enumerate(matches, 1):
        if count == 1: card_price = 1
        card_price *= calculate_price(count)
    price += card_price
    
print(price)