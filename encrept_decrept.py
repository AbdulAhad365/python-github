def decrpt(text,shift,alphabet):
    store=int(input("Enter the shift code for decoding"))
    s = ""
    if(store==shift):
        for x in text:
           index = 0
           while (x!=alphabet[index]):
               if x==alphabet[index]:
                   break
               index = index + 1

           s=s+alphabet[index-shift]
        print(s)
        return s
    return s
def encrypt(text,shift,alphabet):
    index=0
    store=0
    s=""
    for x in text:
        index=0
        while x!=alphabet[index]:
            if x==alphabet[index]:
                break
            store = index
            index=index+1
        #APPLY THE SHIFT
        if x=='a':
            store=store+shift
        else:
            store=store+1+shift
        if(store<=25):
            s=s+alphabet[store]
        else:
            index=(store-26)
            s=s+alphabet[index]
    print(s)
    return s


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrept=encrypt(text,shift,alphabet)
decr=decrpt(encrept,shift,alphabet)
print("Staement= "+decr)



