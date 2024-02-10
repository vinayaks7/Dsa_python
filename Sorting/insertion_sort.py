import sys

def insertion_sort(arr, n):
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            # swap(arr,j,j-1)
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

    return arr

arr=[13, 46, 24, 52, 20, 9]
n=len(arr)

arr=insertion_sort(arr,n)
print(arr)