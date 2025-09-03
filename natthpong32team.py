
def log_result(name, result, attempts):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("game_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{time} | ผู้เล่น: {name} | ผลลัพธ์: {result} | จำนวนครั้งที่ทาย: {attempts}\n") 