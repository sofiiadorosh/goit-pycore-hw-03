from random import sample

MIN_VALUE = 1
MAX_VALUE = 1000

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value < MIN_VALUE or max_value > MAX_VALUE or quantity < min_value or quantity > max_value:
        return []

    return sorted(sample(range(min_value, max_value + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
