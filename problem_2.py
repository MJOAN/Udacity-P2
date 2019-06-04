def rotated_array_search(input_list, number):
    n = len(input_list) - 1 
    pivot = None
    lo = 0
    hi = len(input_list) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if input_list[mid] > input_list[mid + 1]: 
            pivot = mid + 1
            
        if mid + 1 == pivot: 
            break

        if input_list[lo] < input_list[mid]:
            lo = mid + 1 
        else: 
            hi = mid - 1 

    return find_half(input_list, pivot, number)

def find_half(input_list, pivot, number):
    lo = 0
    hi = len(input_list) - 1
    
    first_half = input_list[:lo] + input_list[:pivot]
    second_half = input_list[:pivot] + input_list[:hi]
    
    for num in first_half:
        if num == number:
            return binary_search(first_half, number)
    
    for num in second_half:
        if num == number:
            return binary_search(second_half, number)

def binary_search(half, number):
    lo = 0
    hi = len(half) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if half[mid] == number:
            return mid

        if number < half[mid]:
            hi = mid - 1
        
        else:
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

print('Test 1: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]))
print('Test 1: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]))
print('Test 1: ', test_function([[6, 7, 8, 1, 2, 3, 4], 8]))
print('Test 1: ', test_function([[6, 7, 8, 1, 2, 3, 4], 1]))
print('Test 1: ', test_function([[6, 7, 8, 1, 2, 3, 4], 10]))

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


print('Test 2: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]))
print('Test 2: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]))
print('Test 2: ', test_function([[6, 7, 8, 1, 2, 3, 4], 8]))
print('Test 2: ', test_function([[6, 7, 8, 1, 2, 3, 4], 1]))
print('Test 2: ', test_function([[6, 7, 8, 1, 2, 3, 4], 10]))

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

print('Test 3: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]))
print('Test 3: ', test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]))
print('Test 3: ', test_function([[6, 7, 8, 1, 2, 3, 4], 8]))
print('Test 3: ', test_function([[6, 7, 8, 1, 2, 3, 4], 1]))
print('Test 3: ', test_function([[6, 7, 8, 1, 2, 3, 4], 10]))