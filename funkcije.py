broj = input()

def input_int():
    while True:
        broj = input()
        if broj.isnumeric():
            broj = int(broj)
            break
    return broj
