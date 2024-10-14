roman=input('Enter a roman number: ')
num=0    
dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in range(len(roman)):
    if i+1<len(roman) and dic[roman[i]] < dic[roman[i+1]]:
        num -= dic[roman[i]]
    else:
        num += dic[roman[i]]
print(num)        