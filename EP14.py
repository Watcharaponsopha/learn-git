'''
โครงสร้างควบคุม (Control structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ

'''
age=int(input("ป้อนอายุของคุณ"))

if age>=15:
    print("คำนำหน้าเป็น นาย/นางสาว")
    print("จบโปรแกรมด้านใน if")
else :
    print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")

if age>=15 and age <= 20:
    print("วัยรุ่น")
elif age>=20 and age<=29:  #elif คือการเลือกเพียง 1 ตัวเลือก เช็คตัวแรกก่อนเสมอ
    print("วัยหนุ่มสาว")
elif age>=30 and age<=59:
    print("วัยผู้ใหญ่")
elif age>=60 :
    print("วัยชรา")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")
#15-20 => วัยรุ่น
#21-29=> วัยหนุ่มสาว
#30-39=> วัยผู้ใหญ่
print("-วัยรุ่น") if age>=15  else print("-วัยเด็ก")