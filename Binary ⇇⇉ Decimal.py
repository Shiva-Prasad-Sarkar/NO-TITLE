#Decimal to Binary and Binary to Decimal
conversion = input('Press 1 for binary to decimal otherwise Press 2 for decimal to binary conversion:)')

if conversion == 2:
    dec = input('Enter the decimal valule: ')
    binary = ''
    k = int(input('Enter the number of digits you want to get after decimal point: '))
    c = 0

    for i in range(len(dec)):
        if dec[i] == ".":
            second = dec[i:len(dec):1]
            first = dec[0:i]

    while c<k:
        second=float(second)*2
        if second<1:
            binary+= '0'
            c+=1
            second=second
        elif second>1:
            binary+= '1'
            second=second-1
            c+=1  
        else:
            binary+= '1'
            break  
                
    first=int(first) 
    binar=''

    while first!= 0:
        if first%2 == 0:
            binar+= '0'
        else:
            binar+= '1'
        first = first//2   
        
    binar=binar[::-1]   
    final=binar+'.'+binary
    print(final)

else:
    bin = input('enter the binary value: ')
    dec = 0.0

    for i in range(len(bin)):
        if bin[i] == ".":
            second = bin[i+1:len(bin):1]
            first = bin[0:i]

    k = len(first)-1
    for i in range(len(first)):
        dec+=int(first[i])*2**k
        k-=1
    
    for j in range(len(second)):
        dec+=int(second[j])/(2**(j+1))
    
    print(dec)

