n=int(input())
b=[]
a=list(map(int,input().split()))
for i in range(n):
    b.append(a[i])
b.extend(a)
print(*(b))