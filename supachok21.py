import random
import datetime

def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def check_guess(answer, guess):
    if guess < answer:
        return "น้อยเกินไป!"
    elif guess > answer:
        return "มากเกินไป!"
    else:
        return "ถูกต้อง!"