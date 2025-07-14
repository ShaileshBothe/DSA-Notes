#Binary Search
'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else: 
            high = mid - 1

    return -1 

# time complexity: O(log n)
# space complexity: O(1)

# Recursive Binary Search

'''

'''
def recursive_binary_search(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return recursive_binary_search(arr, x, mid + 1, high)
    else:
        return recursive_binary_search(arr, x, low, mid - 1)

# time complexity: O(log n)
# space complexity: O(log n) due to recursion stack

'''

'''

# First Occurance of a number in sorted Array

l = [1, 2, 2, 2, 3, 4, 5]

def first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# time complexity: O(n)
# space complexity: O(1)

arrr = [1, 2, 2, 2, 3, 4, 5]
print(first_occurrence(arrr,  2))

'''

'''

# Binary Search for First Occurrence
def binary_search_first_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else: 
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                high = mid - 1

    return -1
# time complexity: O(log n)
# space complexity: O(1)
arrr = [1, 2, 2, 2, 3, 4, 5]
print(binary_search_first_occurrence(arrr, 3))

'''
'''
# Last occurrence of a number in sorted Array
def last_occurrence(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
    return -1
# time complexity: O(n)
# space complexity: O(1)
arrr = [1, 2, 2, 2, 3, 4, 5]
print(last_occurrence(arrr, 2))

#last occurrence using binary search
def binary_search_last_occurrence(arr,x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            if mid == len(arr)-1 or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1
# time complexity: O(log n) 
# space complexity: O(1)
arrr = [1, 2, 2, 2, 3, 4, 5]
print(binary_search_last_occurrence(arrr, 2))

'''