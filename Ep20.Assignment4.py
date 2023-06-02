#แลกเงิน

# 2000 => 2*1000

number = int(input("ป้อนจำนวนเงินของคุณ :"))
if number>= 100:
    print("1000บาท = ",number//1000,"ใบ")
    number%=1000
if number >= 500:
     print("500บาท = ",number//500,"ใบ")
     number%=500
if number >= 100:
         print("100บาท = ",number//100,"ใบ")
         number%=100
if number >= 500:
         print("50บาท = ",number//50,"ใบ")
         number%=50
if number >= 20 :
         print("20บาท = ",number//20,"ใบ")
         number %=20
