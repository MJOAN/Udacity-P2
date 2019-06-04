def sort_012(input_list):
    
    lo = 0
    hi = len(input_list) - 1
    mid = 0  
    
    while mid <= hi:
        if input_list[mid] == 0:
            input_list[lo], input_list[mid] = input_list[mid], input_list[lo]
            # print('lo, mid', input_list[lo], input_list[mid])
            lo += 1
            mid += 1
            continue
        elif input_list[mid] == 2:
            input_list[mid], input_list[hi] = input_list[hi], input_list[mid]
            hi -= 1
            # print('mid, hi', input_list[mid], input_list[hi])
            continue
        else:
            mid += 1
            continue
    return input_list
    

def test_function1(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function1([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function1([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

def test_function2(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function2([0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2, 0, 2])
test_function2([2, 1, 2, 0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 1])

def test_function3(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function3([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function3([2, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 1, 0, 2, 0, 0, 1])

# Citations:
# 1. https://en.wikipedia.org/wiki/Dutch_national_flag_problem 