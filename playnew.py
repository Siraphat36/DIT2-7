def ask_play_again():
    while True:
        choice = input("\nคุณต้องการเล่นอีกครั้งหรือไม่? (พิมพ์ y เพื่อเล่นต่อ / n เพื่อออก): ").strip().lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("กรุณากรอก 'y' เพื่อเล่นต่อ หรือ 'n' เพื่อออก")