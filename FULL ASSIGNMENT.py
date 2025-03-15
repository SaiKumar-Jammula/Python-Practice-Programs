#program to write 10-30
for i in range (10,31):
 print(i,end =" ")
print("\n"
      )
#program to print even numbers from 0-11
for i in range(0,11,2):
 print(i,end =" ")
print("\n")

#program to print 50,45,40,35......,5
for i in range(50,0,-5):
 print(i,end =" ")
print('\n')

#program to print first 5 natural even numbers and their squares using "for" loop
for i in range(2,11,2):
 print(i,end=" ")
 print(i*2)

 #print sum of first 5 odd natural numbers using "for" loop
sum=0
for i in range(1,10,2):
 sum += i
 print(sum)

 #print table using "for" loop and accept table number from user
print("enter the table")
n=int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    print("\n")

#print factorial of a number using "for" loop
n=int(input("ENTER FACTORIAL NUMBER:"))
fact=1
for i in range(1,n+1):
       fact *= i
print(fact)

#WAP for below mentioned conditions using logical operator?
print("ENTER THE MARKS")
n=int(input())
if n>=90:
    print("EXCELLENT")
elif n>=80:
    print("GOOD")
elif n>=65:
    print("BETTER")
elif n<=35:
    print("FAIL")

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
   
   #WAP to find smallest number among three numbers using logical operator?
num1=int(input("enter 1st num :"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if (num1<num2) and (num1<num3):
 print("NUM1 IS SMALLEST")

elif (num2<num3) and (num2<num1):
   print("NUM2 IS SMALLEST")
else :
   print("NUM3 IS SMALLEST")


