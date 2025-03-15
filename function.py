a=int(input())
b=int(input())
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("ENTER YOUR CHOICE :")
print("1.ADD")
print("2.SUB")
print("3.MULTIPLY")
print("4.DIVIDE")

while True:
 choice=input()
if choice==1:
    print(add(a,b))
