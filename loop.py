def main():
    while True:
        play_game()
        if not ask_play_again():
            print("👋 ขอบคุณที่เล่นเกม! แล้วพบกันใหม่ครั้งหน้า!")
            break

if name == "main":
    main()