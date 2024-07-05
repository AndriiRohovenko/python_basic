import random


def get_numbers_ticket(min_num, max_num, quantity):
    try:
        # Validate input parameters
        if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1) or quantity < 1:
            return []
        
        # Generate unique random numbers and sort
        numbers = random.sample(range(min_num, max_num + 1), quantity)
        numbers.sort()
        
        return numbers
    except Exception as ex:
        print(f"An unknown error has occurred! {ex}")