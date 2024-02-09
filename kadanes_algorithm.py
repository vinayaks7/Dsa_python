import sys

def kadanealgo(arr,n):
    maxsum=-sys.maxsize-1
    sum=0
    for i in range (n):
        sum+=arr[i]
        if sum>maxsum:
            maxsum=sum
        if sum<0:
            sum=0
    return maxsum

arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
n=len(arr)
ans=kadanealgo(arr,n)
print(ans)