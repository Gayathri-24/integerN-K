n=int(input("Enter a size:"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
k=int(input("Enter index value"))
sum=0
for i in range(0,k):
    sum=sum+int(arr[i])
print(sum)

