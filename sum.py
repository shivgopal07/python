k=int(input("Enter the no."))
sum=0
while(k>0):
    dig=k%10
    sum=sum+dig
    k=k//10
print(sum)
