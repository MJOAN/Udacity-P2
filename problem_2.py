# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# You are given a target value to search. 
# If found in the array return its index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's 
# runtime complexity must be in the order of O(log n).
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

def rotated_array_search(input_list, number):
    n = len(input_list) - 1 
    pivot = None
    lo = 0
    hi = len(input_list) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        print('start mid', mid)
        if input_list[mid] > input_list[mid + 1]: 
            print('pivot', pivot)
            pivot = mid + 1
            
        if mid + 1 == pivot: 
            print('pivot', pivot)
            break

        if input_list[lo] < input_list[mid]:
            print('lo', lo)
            lo = mid + 1 # so we can look for pivot in second 1/2 
        else: 
            print('hi', hi)
            hi = mid - 1 # so we can look for pivot in first 1/2

    return find_half(input_list, pivot, number)

def find_half(input_list, pivot, number):
    lo = 0
    hi = len(input_list) - 1
    
    first_half = input_list[:lo] + input_list[:pivot]
    second_half = input_list[:pivot] + input_list[:hi]
    
    print('first half', first_half)
    print('second half', second_half)

    for num in first_half:
        if num == number:
            print('num in 1st half', number, first_half, lo, hi)
            return binary_search(first_half, number)
    
    for num in second_half:
        if num == number:
            print('num in 2nd half', number, second_half, lo, hi)
            return binary_search(second_half, number)

def binary_search(half, number):
    lo = 0
    hi = len(half) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if half[mid] == number:
            print('mid', mid)
            return mid

        if number < half[mid]:
            print('hi', hi)
            hi = mid - 1
        
        else:
            print('lo', lo)
            lo = mid + 1
    
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print('first-test', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]))
print('first-test', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]))
print('first-test', test_function([[6, 7, 8, 1, 2, 3, 4], 8]))
print('first-test', test_function([[6, 7, 8, 1, 2, 3, 4], 1]))
print('first-test', test_function([[6, 7, 8, 1, 2, 3, 4], 10]))

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])