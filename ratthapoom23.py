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
            print(f"ยินดีด้วย {player_name}! คุณชนะแล้ว!")
            log_result(player_name, "ชนะ", attempts)
            break
    else:
        print(f"คุณแพ้! คำตอบที่ถูกต้องคือ {number_to_guess}")
        log_result(player_name, "แพ้", attempts)