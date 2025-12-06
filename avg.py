def calculate_average(l):
    ans=0
    for i in range(len(l)):
        ans+=l[i]
    return ans/len(l)
l=list(map(int,input().split()))
print(calculate_average(l))

