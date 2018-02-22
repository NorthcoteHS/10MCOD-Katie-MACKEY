al = 'abcdefghijklmnopqrstuvwxyz'
m = input("Select: 1 - Encode or 2 - Decode ")
while m != "":
    if int(m) == 1:
        p = input("Plaintext: ")
        k = input("Key: ")
        c = []
        i = 0
        #make it lowercase
        p = p.lower()
        k = k.lower()
        #making the key
        a,b = divmod(len(p),len(k))
        k2 = k*a + k[:b]
        '''shifting plaintext (formula is (p+k)%26) with p and k being being nth
        or ith in this case) letter of the plaintext and the key'''
        while i < len(p):
            c.append(al[(al.find(p[i])+al.find(k2[i]))%26])
            i += 1
        #letters are added to a list then joined together
        print("".join(c))
        m = input("Select: 1 - Encode or 2 - Decode ")
    elif int(m) == 2:
        c = input("Ciphertext: ")
        k = input("Key: ")
        p = []
        i = 0
        #make it lowercase
        c = c.lower()
        k = k.lower()
        #making the key
        a,b = divmod(len(c),len(k))
        k2 = k*a + k[:b]
        '''shifting plaintext (formula is (p+k)%26) with p and k being being nth
        or ith in this case) letter of the plaintext and the key'''
        while i < len(c):
            p.append(al[(al.find(c[i])-al.find(k2[i]))%26])
            i += 1
        #letters are added to a list then joined together
        print("".join(p))
        m = input("Select: 1 - Encode or 2 - Decode ")
    else:
        print("Not an option. Please try again")
        m = input("Select: 1 - Encode or 2 - Decode ")
import sys
sys.exit()
