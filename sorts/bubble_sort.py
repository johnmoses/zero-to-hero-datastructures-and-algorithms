""" 
Bubble Sort is an algorithm that sorts an array from the 
lowest value to the highest value
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [64, 34, 25, 12, 22, 11, 90, 5]
array1 = ['E','F','A','G','C','B','D']

print(bubble_sort(array))
print(bubble_sort(array1))

def bubble_sort_1(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort_1(array))
print(bubble_sort_1(array1))