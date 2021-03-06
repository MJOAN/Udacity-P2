def rotated_array_search(input_list, number):
    
    lo = 0
    hi = len(input_list) - 1
    
    while lo <= hi:
        mid = (lo + hi)//2
        
        if number == input_list[mid]:
            return mid
        
        if input_list[mid] >= input_list[lo]:
            if number < input_list[mid] and number >= input_list[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        elif input_list[mid] < input_list[hi]:
            if number > input_list[mid] and number <= input_list[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1     

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function1(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function1([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function1([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function1([[6, 7, 8, 1, 2, 3, 4], 8])
test_function1([[6, 7, 8, 1, 2, 3, 4], 1])
test_function1([[6, 7, 8, 1, 2, 3, 4], 10])

def test_function2(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function2([[5, 6, 7, 8, 1, 2, 3, 4], 2])
test_function2([[4, 5, 6, 7, 1, 2, 3, 4], 1])
test_function2([[3, 4, 5, 6, 1, 2], 3])

def test_function3(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function3([[5, 6, 7, 1, 2, 3, 4], 6])
test_function3([[4, 5, 6, 1, 2, 3], 1])
test_function3([[3, 4, 5, 6, 7, 8, 1, 2], 8])