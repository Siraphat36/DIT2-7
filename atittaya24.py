#ใส่ชื่อ
name = input("กรุณากรอกชื่อของคุณ: ")
#ใส่ปีเกิด
year_buddhist = int(input("กรุณากรอกปี พ.ศ. ที่เกิด: "))
#แปลงปี พ.ศ. เป็นปี ค.ศ.
year_christ = year_buddhist - 543
current_year = 2025
#เอาปี ค.ศ. ปัจจุบันมาลบกับปีที่เกิด
age = current_year - year_christ
#ผลลัพธ์
print(name+f" อายุปัจจุบันของคุณคือ {age} ปี")