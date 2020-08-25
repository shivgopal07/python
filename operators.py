a=int(input('enter the number'))
b=int(input('enter the number'))
print('1.addtion\n2.subtraction\n3.multiplication\n4.division\n5.modules\n6.exponent\n7.floor division\n0.exit')
ch=int(input('enter your choice'))
if ch==1:
    c=a+b
    print('sum',c)
if ch==2:
    c=a-b
    print('sub',c)
if ch==3:
    c=a*b
    print('multipy',c)
if ch==4:
    c=a/b
    print('divide',c)
if ch==5:
    c=a%b
    print('module',c)
if ch==6:
    c=a**b
    print('expo',c)
if ch==7:
    c=a//b
    print('floor division',c)
if ch==0:
    print(exit)
