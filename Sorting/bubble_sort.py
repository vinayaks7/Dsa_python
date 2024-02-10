import sys

# reversed range
# for num in reversed(range(N + 1)) :
#     print(num, end = " ")

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    return  arr

def bubble_sort_algo(arr,n):
    for i in range(n-1,0,-1):
        did_swap=0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                did_swap=1
                arr=swap(arr,j,j+1)

        if did_swap==0:
            break
    return arr



arr=[13, 46, 24, 52, 20, 9]
n=len(arr)

arr=bubble_sort_algo(arr,n)
print(arr)