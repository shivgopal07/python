a=int(input('enter the year'))
if(a%400==0 or (a%100!=0 and a%4==0)):
    print('it is leap year')
else :
    print('it is not a leap year')
    
