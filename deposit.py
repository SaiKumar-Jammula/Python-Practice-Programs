def deposit():
    while True:
        amount=input("What would you like to deposit ?")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
               break
            else:
                print("Enter amount greater than zero")
        else:
            print("Please enter a number")
    return amount
deposit()
 