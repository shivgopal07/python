#GCD
num1=int(input('enter the number'))
num2=int(input('enter the number'))
i=1
while i<=num1:
    if (num1%i==0) and (num2%i==0):
        k=i
    i=i+1
print(k)
