def sum_of(x):
    sum=0
    while(x>0):
        dig=x%10
        sum=sum+dig
        x=x//10
        b=sum
    return(b)




x=int(input("Enter the no."))
while(x>0):
    sum_of(x)
print(x)
