def line_splitter(line: str):
    card_id, numbers = line.split(": ")
    card_id = card_id.strip().split()
    numbers = numbers.strip().split("|")    
    return int(card_id[1]), numbers

def update_copies(card_id: int, c: int):
    c_id = card_id
    c_id += c
    all_cards[c_id] += 1

all_cards = {i: 1 for i in range(1, 198)}

while True:
    line = input()
    if line == '':
        break
    card_id, numbers = line_splitter(line)
    winning_numbers = set(map(int, numbers[0].split()))
    other_numbers = set(map(int, numbers[1].split()))
    matches = winning_numbers.intersection(other_numbers)

    for c in range(1, len(matches)+1):
        update_copies(card_id, c)
        copies = all_cards[card_id]
        if copies > 1:
            for copy in range(1, copies):
                update_copies(card_id, c)
    
print(sum(all_cards.values()))