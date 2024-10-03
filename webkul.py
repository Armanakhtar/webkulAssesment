n=int(input("Enter odd no: "))
if n%2==0 or n<=2:
    print("invalid")
else:
    for i in range(n//2+1):
        for sp in range(n):
            print(end=" ")

        for j in range(n,i,-1):
            print("",end=" ")

        
        for k in range(i*2-1):
            print("*",end="")
        print()

    print(" "* (n//2),"e"*n,"*"*n,"e"* n, sep="")

    for i2 in range(n):
        for sp2 in range(n//2):
            print(end=" ")
        print("e",end="")
        print(" "* (n*3-2),"e",sep="")

        if i2==(n-1):
            print("*"* n," "* ((n*2)-1),"*"*n,sep="")
    

            

n=5
f_l=n//2+1
center=(4*n)//2
for i in range(0,f_l,1):
    for j in range(0,4*n,1):
        if(center<=j and j<= (4*n)-center):
            print("*",end="")
        elif(i==n//2 and j>=f_l and j<=(4*n)-f_l):
            print("e",end="")
        else:
            print(" ",end="")
    center=center-1
    print()
for i in range(0,n+1,1):
    for j in range(0,4*n,1):
        if((n//2+1==j and i<n) or (j==(3*n)+(n//2) and i<n)):
            print("e",end="")
        elif(n==i and n+1>j and j>0) or ( n==i and j>=(3*n) and j<(n*4)):
            print("e",end="")
        else:
            print(" ",end="")
    print()



# n=int(input("Enter odd no: "))
n=13
hn=n//2
a=1
if n%2==0 or n<=2:
    print("invalid")
else:
    for i in range(1,hn+1):
        for j in range(i):
            if j==0:
                print(" "*((n*4)-hn),end="")
            print("*",end="")
        print()
    print(" "*((n*2)-hn),'*'*n,"e"*n,"*"*((hn)+1),sep="")
    for i in range(1,n-1):
        if i>=n//2:
            for _ in range(0,n-i-1):
                print(" ",end="")
            for _ in range(a):
                print("*",end="")
        else:
            print(" "*(hn+1),end="")
        print(" "*n,"*"*n," "*n,sep="",end="")
        for j in range(hn-i+1):
            print("*",end="")
        if(i>=n-i-1):
            a=a+1
        print()
    else:
        print("*"*(hn+1),"e"*n,"*"*n,sep="",end="\n")
        for i in range(1,hn+2):
            for sp in range(0,i):
                print(" ",end="")
            for j in range(0,(hn+1)-i):
                print("*",end="")
            print()