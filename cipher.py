alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v', 'w','x', 'y','z']
def encrypt(org_txt,step):
    cipher_txt=''
    for char in org_txt:
        if char in alphabets:
            ind_org_txt=alphabets.index(char)
            new_ind=(ind_org_txt+step)%26
            cipher_txt+=alphabets[new_ind]
        else:
            cipher_txt += char
    capital=cipher_txt.upper()
    print(capital)
def decrypt(org_txt,step):
    cipher_txt=''
    for char in org_txt:
        if char in alphabets:
            ind_org_txt=alphabets.index(char)
            new_ind=(ind_org_txt-step)%26
            cipher_txt+=alphabets[new_ind]
        else:
            cipher_txt += char
    capital=cipher_txt.upper()
    print(capital)
optionofuser=True
while optionofuser:
    print("----------------CEASER CIPHER----------------")
    option=input("Enter the operation to do(encrypt/decrypt)\n").lower()
    org_txt=input("Enter the text :\n").lower()
    step=int(input("Enter the shift :\n"))
    if option == 'encrypt':
        encrypt(org_txt,step)
    elif option== 'decrypt':
        decrypt(org_txt,step)
    playagain=input("DO YOU WANT TO CONTINUE(YES/NO)").lower()
    if playagain=="no":
        optionofuser=False
