a = input()
c1 = 0
c2 = 0
c3 = 0
flag = True
for i in a:
    if i=='(':
        c1+=1
    elif i=='{':
        c2+=1
    elif i=='[':
        c3+=1
    elif i==')':
        c1-=1
    elif i=='}':
        c2-=1
    else:
        c3-=1
    if c1<0 or c2<0 or c3<0:
        print('invalid')
        flag = False
        break
if c1==c2==c3==0 and flag==True:
    print('valid')
    