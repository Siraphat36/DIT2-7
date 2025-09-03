def get_user_guess():
    while True:
        try:
            guess = int(input("กรุณาเดาตัวเลข (1-100): "))
            return guess
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")
