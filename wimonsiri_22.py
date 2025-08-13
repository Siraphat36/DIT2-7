from datetime import datetime
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y")
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
you_name = input("กรอกชื่อ: ")
bc_born = input("กรอกป๊เกิด : ")
age = calculate_age(bc_born)
print(f" คุณ {you_name} คุณมีอายุ {age} ปี")