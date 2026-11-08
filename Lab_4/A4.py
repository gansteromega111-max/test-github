import re
def is_valid_number(card_number):
    return card_number.isdigit() and len(card_number) in [13, 15, 16]
def get_check_sum(card_number):
    check_sum = 0
    for i in reversed(range(0, len(card_number) - 1, 2)):
        product = int(card_number[i]) * 2
        if product > 9:
            check_sum = check_sum + 1 + product - 10
        else:
            check_sum = check_sum + product
    for i in reversed(range(1, len(card_number) + 1, 2)):
        check_sum += int(card_number[i])
    return check_sum
def get_card_type(string):
    if len(string) == 13 or (len(string) == 16 and string.startswith("4")):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid"
if __name__ == "__main__":
    card_number = input("Enter Card Number: ")
    if is_valid_number(card_number):
        if get_check_sum(card_number) % 10 == 0:
            print("Valid")
            print(get_card_type(card_number))
        else:
            print("Invalid Checksum")
    else:
        print("Wrong Input. Try again...")