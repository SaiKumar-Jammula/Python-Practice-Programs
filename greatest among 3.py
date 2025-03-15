#WAP to find greatest number among three numbers using nested if?
num1=int(input("enter 1st num :"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if (num1>num2) and (num1>num3):
 print("NUM1 IS GREATEST")

elif (num2>num3) and (num2>num1):
   print("NUM2 IS GREATEST")
else :
   print("NUM3 IS GREATEST")