def countBits(num): # function take paramater from code below
    tempBi = ""   #create str tempbi for get remainder from code below
    bit = 0         #create variable int for count bits
    while num > 0:      #using loop because count one by one till the end of bits
        tempBi = num % 2    #num get from print will divided and give remaind to tempBi looping
        num //= 2   #num = num divided by 2 becasue one remaind value minus one number from right to left looping
        if tempBi > 0:  #using if when remainder = 1 mean greater than 0
            bit += 1  #if so bit count 1 looping
        else:  #else :
            continue  #skip it and countinue looping
    return bit  #return total bits
print(countBits(1234))  #print and take 1234 to num function