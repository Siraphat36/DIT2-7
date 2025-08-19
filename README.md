# DIT2-7
คำสั่งในการใช้ (เผื่อลืม)
1. git pull origin [ชื่อ Branch] 
2. git add [ชื่อ ไฟล์.นามสกุล] //หรือใช้ . แทนชื่อไฟล์ก็ได้เพื่อแทนไฟล์ทั้งหมด
3. git commit -m '[คอมเม้น]'
4. git push [ชื่อไฟล์.นามสกุล] origin [ชื่อ Branch] //กรณีที่จะ push ไฟล์ทั้งหมดไม่จำเป็นต้องใส่ชื่อไฟล์ก็ได้
5. git HEAD [ชื่อไฟล์.นามสกุล]
6. git branch '[ชื่อ Branch/คำอธิบาย]' //ไม่จำเป็นต้องใส่คำอธิบาย
7. git checkout [ชื่อ Branch/คำอธิบาย] //บาง Branch ไม่มีคำอธิบายเลยไม่ต้องใส่เอาตามที่ชื่อมันมี
8. git log
9. git merge [ชื่อ Branch ที่ต้องการจะ Merge ไปกับ Main]

ทำอะไรได้

1.คำสั่งดึงข้อมูลมาจาก Repo
2.เอาคำสั่งที่แก้ไขสำเร็จแล้วไปวางที่ Staging Area
3.คำสั่งยืนยันว่าจะส่ง
4.คำสั่งส่ง
5.ยกเลิกหรือ Reset การ commit
6.คำสั่งสร้าง Branch
7.คำสั่งย้าย HEAD ไปที่ Branch อื่น
8.ตรวจสอบข้อและเวอร์ชั่นของการ Commit
9.คำสั่งที่เอาbranchที่เราอยู่ไปรวมกับbranchอีกอัน

คำสั่งลบ Branch มี 2 แบบ Local,Remote Project
Local
git branch -d [ชื่อ Branch]
Remote Project
git push --delete origin [ชื่อ Branch ที่จะลบ]

