#while True:
sum_odd_digits=0
sum_even_digits=0
total=0


card_num=input("Enter card number: ")
str_card=card_num
card_num=card_num.replace('-',"")
card_num=card_num.replace(' ',"")
card_num=card_num[::-1]
for x in card_num[::2]:
    sum_odd_digits+=int(x)
for x in card_num[1::2]:
    mul=int(x)*2
    if mul>=10:
        sum_even_digits+=(1+(mul%10))
    else:
        sum_even_digits+=mul
total=sum_even_digits+sum_odd_digits
if total%10 == 0:
    print("THE CARD IS VALID")
if len(card_num)==14 and str_card[:2]=='37':
    print("IT IS AMERICAN EXPRESS CARD")

else:
    print("THE CARD IS INVALID")






