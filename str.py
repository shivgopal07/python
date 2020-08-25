st=input('enter the string: ')
print('1.Total no of charcter\n2.Last threee digit\n3.print the string backword direction\n4.The string in all CAPITAL LETTER')
ch=int(input('enter the choice'))

if ch==1:
       length=len(st)
       print(length)


if ch==2:
       print('str[-3: ]',st[-3:])



if ch==3:
       print('str[ ::-1]',st[ ::-1])



if ch==4:
       st=st.uppercase()
       
