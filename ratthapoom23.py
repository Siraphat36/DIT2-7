from datetime import datetime
N = input("ชื่อ ")
B = input("ใส่วันเกิด (ใส่แบบ DD/MM/YYYY) ")
S = datetime.strptime(B, "%d/%m/%Y")
O = datetime.today()
L = O.year - S.year
print("ชื่อ ", N , "อายุ", L , "ปี")