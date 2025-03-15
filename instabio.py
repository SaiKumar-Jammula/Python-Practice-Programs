alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(org_txt, step):
    cipher_txt = ''.join(alphabets[(alphabets.index(char) - step) % 26] for char in org_txt if char in alphabets)
    print('\n'.join(cipher_txt))

decrypt('ixfnbrxelwfk', 3)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(org_txt, step):
    cipher_txt = ''
    for char in org_txt:
        if char in alphabets:
            ind_org_txt = alphabets.index(char)
            new_ind = (ind_org_txt - step) % 26
            cipher_txt += alphabets[new_ind]
    for i in cipher_txt:
        print(i)

decrypt('ixfnbrxelwfk', 3)


