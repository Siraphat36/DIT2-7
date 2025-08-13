# test
import random
number = random.randint(1, 100)
print("ทายเลขระหว่าง 1 ถึง 100")

while True:
    guess = int(input("ใส่เลขที่คุณทาย: "))
    if guess < number:
        print("น้อยเกินไป")
    elif guess > number:
        print("มากเกินไป")
    else:
        print("ถูกต้อง! เลขคือ", number)
        break