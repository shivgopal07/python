m=int(input("enter the length: "))
n=int(input("enter the breath: "))
def rect(m,n):
    for i in range (m):
        for j in range (n):
            print("*",end="")
        print()
rect(m,n)
