n=3

if n%2==0 or n==1:
    print("Enter odd no")
else:
    for i in range (n//2+1):
        print(" "*(n//2+1),end="")
        for _ in range(i,n//2):
            print(" ",end="")
        for _ in range(i*2+1):
            print("*",end="")
        print()

    for j in range(n):
        print(" "*(n//2),'e'," "*(n),"e",sep="")


    for j in range(n//2+1):
        for _ in range(j):
            print(" ",end="")
        for _ in range(j*2,n):
            print("*",end="")
        
        print(" ",end="")

        for _ in range(j*2):
            print(" ",end="")
        for _ in range(j*2,n):
            print("*",end="")
        print()
   