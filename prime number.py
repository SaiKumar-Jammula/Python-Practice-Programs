num=int(input("Enter the number"))
lim=int(num/2+1)
for i in range(2,lim):
    rem=num%i
    if rem==0:
        print(num,"is not prime number")
        break
else:
    print(num,"number is prime number")
            
