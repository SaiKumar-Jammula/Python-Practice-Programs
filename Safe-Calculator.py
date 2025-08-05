def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def sub(x, y):
    return x - y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

while True:
    try:
        usr_input = int(input("Enter your operation \n 1. Add \n 2. Multiply \n 3. Subtract \n 4. Divide \n 5. Exit\n"))
        
        if usr_input == 5:
            print("Exiting the calculator.")
            break
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if usr_input == 1:
            print("The addition result is", add(num1, num2))
        elif usr_input == 2:
            print("The multiplication result is", mul(num1, num2))
        elif usr_input == 3:
            print("The subtraction result is", sub(num1, num2))
        elif usr_input == 4:
            result = div(num1, num2)
            if result is not None:
                print("The division result is", result)
        else:
            print("Enter a valid option.")
    
    except ValueError:
        print("Error: Enter only numbers.")
    except Exception as e:
        print("Exception occurred:", e)
    finally:
        print("Thank you for using the safe calculator.\nRestarting...\n")



         
         
         

       


