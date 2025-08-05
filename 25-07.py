def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    try:
     return x/y
    except ZeroDivisionError:
       print("cannot be divided by 0")


while True:
    usr_input=int(input("Enter your operation \n 1.add \n 2.mul \n 3.sub \n 4.div\n 5.exit\n"))
    if usr_input == "5":
        print("exiting the calculator ")
        break
    try:
        num1=int(input("enter first num : "))
        num2=int(input("enter second num : "))

        if usr_input==1:
            print("The addition result is ",add(num1,num2))
        elif usr_input==2:
            print("The multiplication result is ",mul(num1,num2))
        elif usr_input==3:
            print("The subtarction result is ",sub(num1,num2))
        elif usr_input==4:
            print("The division result is ",div(num1,num2))
        else:
            print("Enter Valid Input ")
    except ValueError:
        print("error :enter only numbers")
    except ZeroDivisionError:
        print("error :cannot be divided by zero")
    except Exception as e:
        print("exception occured ,", e)
    finally:
        print("thank you for using safe calculator.....\n restarting...")


         
         
         

       


