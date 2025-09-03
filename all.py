mport random
import datetime

--------------------- ฟังก์ชันหลักของเกม ---------------------
def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def check_guess(answer, guess):
    if guess < answer:
        return "น้อยเกินไป!"
    elif guess > answer:
        return "มากเกินไป!"
    else:
        return "ถูกต้อง!"

--------------------- รับค่าจากผู้เล่น ---------------------
def get_user_guess():
    while True:
        try:
            guess = int(input("กรุณาเดาตัวเลข (1-100): "))
            return guess
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")

--------------------- แสดงข้อความ ---------------------
def show_welcome():
    print("\n🎉 ยินดีต้อนรับสู่เกมทายตัวเลข! 🎉")
    print("ทายตัวเลขที่คอมพิวเตอร์สุ่มไว้ ระหว่าง 1 ถึง 100")
    print("คุณมีโอกาสทายทั้งหมด 7 ครั้ง\n")

def show_result_message(message):
    print(message)

--------------------- ตรวจสอบช่วงของเลข ---------------------
def validate_range(guess, min_val=1, max_val=100):
    return min_val <= guess <= max_val

--------------------- บันทึกผลลัพธ์ ---------------------
def log_result(name, result, attempts):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("game_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{time} | ผู้เล่น: {name} | ผลลัพธ์: {result} | จำนวนครั้งที่ทาย: {attempts}\n")

--------------------- ฟังก์ชันเล่นใหม่ ---------------------
def ask_play_again():
    while True:
        choice = input("\nคุณต้องการเล่นอีกครั้งหรือไม่? (พิมพ์ y เพื่อเล่นต่อ / n เพื่อออก): ").strip().lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("กรุณากรอก 'y' เพื่อเล่นต่อ หรือ 'n' เพื่อออก")
--------------------- ฟังก์ชันเกมหลัก ---------------------
def play_game():
    show_welcome()
    player_name = input("กรุณากรอกชื่อของคุณ: ")
    number_to_guess = generate_number()
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_guess()
        if not validate_range(guess):
            print("ตัวเลขนอกช่วง! กรุณาเลือกตัวเลขระหว่าง 1 ถึง 100")
            continue

        attempts += 1
        result = check_guess(number_to_guess, guess)
        show_result_message(result)

        if result == "ถูกต้อง!":
            print(f"🎉 ยินดีด้วย {player_name}! คุณชนะแล้ว!")
            log_result(player_name, "ชนะ", attempts)
            break
    else:
        print(f"😢 คุณแพ้! คำตอบที่ถูกต้องคือ {number_to_guess}")
        log_result(player_name, "แพ้", attempts)

--------------------- วนเล่นเกม ---------------------
def main():
    while True:
        play_game()
        if not ask_play_again():
            print("👋 ขอบคุณที่เล่นเกม! แล้วพบกันใหม่ครั้งหน้า!")
            break

if name == "main":
    main()