
import string , random
def gen_password(length=12):
    if len < 4:
        raise ValueError("Password length must be greater than 4")

    upper_case =string.ascii_uppercase
    lower_case =string.ascii_lowercase
    digits =string.digits
    spcl_characters="@!#$%^&*_+.,"
    password=[
    random.choice(upper_case)+random.choice(lower_case)+random.choice(digits)+random.choice(spcl_characters)
    ]
    all_characters=upper_case+lower_case+digits+spcl_characters
    password=password+random.choices(all_characters ,k=len-4)
   


    random.shuffle(password)
    return "".join(password)

try:
    len = int(input(" Enter the length of your password ( min 4) :"))
    password_gen=gen_password(len)
    print("the generated password is ", password_gen)
except Exception as e :
    print("exception occured : " , e)