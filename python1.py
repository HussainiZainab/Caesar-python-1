def caesarCipher ():
    myString = input("What string whould you like me to encrypt?")
    shiftAmt = int(input("Give me a shift amount"))
    cipherString = ""
    
    for c in myString:
        if c.isalpha():
             asciivalue = ord(c)
             asciivalue += shiftAmt
            
             if asciivalue > ord("z"):
                asciivalue-=26

             if asciivalue < ord("a"):
                asciivalue+=26
                
             x = chr(asciivalue)
             cipherString += x
    print(cipherString)

if __name__== "__main__":
    caesarCipher ()
