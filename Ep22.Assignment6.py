#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (Kg)/ ส่วนสูง * ส่วนสูง (m)

weight=float( input("ป้อนน้ำหนักของคุณ(kg):"))
high=float (input("ป้อนสว่นสูงของคุณ(cm):"))
#process
#cm => m
high/=100
bmi=weight/(high**2)

if bmi<18.0 :
    result = "ผอม"
elif bmi>=18.5 and bmi <=22.9:
    result = "สมส่วน"
elif bmi>=23.0 and bmi <=24.9:
    result = "น้ำหนักเกิน"
elif bmi>=25.0 and bmi <=29.9:
    result = "โรคอ้วนระดับ 1 "
elif bmi>30:
    result = "โรคอ้วนระดับ 2 "
else :
    result = "ไม่ทราบค่าที่ชัดเจน"

print("ค่า BMI=",bmi)
print(result)