n=4
c=0
c1=n-1
if n%2==1 or n<2:
    print("Invailid")
else:
    for i in range(1,n*2+1):
        if i<=n/2:
            print("@")
        elif i>=n/2+1 and i<=n+1:
            print("@",end="")
        else:
            print(" ",end="")
        if i>=n/2+1 and i<=((n*2)-n/2):
            print(" "*(n*c-c),end="")
            print("*"*n,end="")
            print(" "*(n*c1-c1),end="")
            if i>=n:
                print("@")
            else:
                print()
            c1-=1
            c+=1
        elif i>n+n/2:
            print(" "*(n*c-c),end="")
            print(" @")