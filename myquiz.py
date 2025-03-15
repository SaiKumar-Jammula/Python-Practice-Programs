

print("Welcome to quiz")
name=input("Enter your name : ")
print("Hello",name,"....Welcome")

score=0 
answer=input("Which IPL Franchise has most loyal fans ? ").upper()
if answer == "RCB":
    print(answer,"Has More Loyal Fans Than Other Teams")
    score+=1
else:
    print("It is incorrect")

answer=input("Which IPL Franchise has won more trophies? ").upper()
if answer == "CSK":
    print(answer,"has won more trophies. ")
    score+=1
else:
    print("It is incorrect")

answer=input("Which IPL Franchise won tropie on his debut match ? ").upper()
if answer == "GT":
    print(answer,"won tropie on his debut match . ")
    score+=1
else:
    print("It is incorrect")

answer=input("Which IPL team scored highest total ? ").upper()
if answer == "SRH":
    print(answer," scored highest total. ")
    score+=1
else:
    print("It is incorrect")
print("congractulations,your have answered",score,"questions correctly")
print("your total score is :",score*100/4)