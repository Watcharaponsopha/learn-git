#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (Kg)/ ส่วนสูง * ส่วนสูง (m)

weight=float( input("ป้อนน้ำหนักของคุณ(kg):"))
high=float (input("ป้อนสว่นสูงของคุณ(cm):"))
#process
#cm => m
high/=100
bmi=weight/(high**2)
#output
print("BMI =",bmi)