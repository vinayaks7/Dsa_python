import sys

def selection_sort_func(arr,n):
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        temp=arr[i]
        arr[i]=arr[mini]
        arr[mini]=temp
    return arr

# arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr=[13,46,24,52,20,9]
n=len(arr)
arr=selection_sort_func(arr,n)
print(arr)