def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True     
n=int(input())
if prime(n):
    print("prime number")
else:
    print("not prime number")  