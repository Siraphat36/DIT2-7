import random

def guess_the_number():
    print("ยินดีต้านรับ")
    print("ให้เดาเลขระหว่าง 1 - 100")

    # คอมพิวเตอร์สุ่มเลข
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # รับค่าจากผู้เล่น
        try:
            guess = int(input("เดาเลย: "))
            attempts += 1

            # ตรวจสอบคำทาย
            if guess < number_to_guess:
                print("น้อยเกินไป.")
            elif guess > number_to_guess:
                print("สูงเกินไป.")
            else:
                print(f"ยินดีด้วยคุณทายถูกแล้ว {number_to_guess} in {attempts} attempts.")
                break

# เรียกใช้ฟังก์ชัน
guess_the_number()
