#decToBi
#MATTHEW ZELLER
#06/19/17
#PHYS 428

#problem 4

def decToBi(xji, xjf = 1.):
    #converts decimal to binary numbers
    #xji is the decimal number initially
    #xjf is the integer quotient
    
    #identify decimal number for output
    print(xji)
    print('-------------')
    print('')
    
    #integer divide decimal number repeatedly
    #remainder is binary value 
    while xjf != 0:
        xjf = xji // 2
        
        #remainder
        print(xji % 2)
        
        xji = xjf
    print('Read from bottom to top')
    print('')

decToBi(56)

decToBi(1543)        
        