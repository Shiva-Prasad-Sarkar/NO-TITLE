def Autocapitalize(string):
    s='.!?'
    a=''
    b=string[0].upper()
    for i in range (len(string)):
        
        if string[i] in s:
            if i+1==len(string):
                break
            elif string[i+1]==' ':
                a=(string[i+2]).upper()
                string=string[:i+2]+a+string[i+3::]
            else:
                a=(string[i+1]).upper()
                string=string[:i+1]+a+string[i+2::]
                
    string=b+string[1::]
        
    for j in range(1,len(string)):
        if string[j]=='i' and (string[j-1]==' ' or string[j+1]==' ') and (string[j-1]==' ' or string[j+1] in s):
            string=string[:j:]+'I'+string[j+1::]
        
    print(string)

sentece = input() 
Autocapitalize(sentece)