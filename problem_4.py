# Dutch National Flag Problem
# Given an input array consisting on only 0, 1, and 2, 
# sort the array in a single traversal in O(n)
# You're not allowed to use any sorting function that Python provides.

def sort_012(input_list):
    
    lo = 0
    hi = len(input_list) - 1
    mid = 0  # (lo + hi) // 2
    
    # if number == 0 we swap lo and mid to LEFT side of 1 & lo/mid += 1
    # if number == 2 we swap mid and hi to RIGHT side of 1 & hi -=1 
    # if number == 1 we keep as is 
    
    while mid <= hi:
        if input_list[mid] == 0:
            input_list[lo], input_list[mid] = input_list[mid], input_list[lo]
            print('lo, mid', input_list[lo], input_list[mid])
            lo += 1
            mid += 1
            continue
        elif input_list[mid] == 2:
            input_list[mid], input_list[hi] = input_list[hi], input_list[mid]
            hi -= 1
            print('mid, hi', input_list[mid], input_list[hi])
            continue
        else:
            mid += 1
            continue
    return input_list
    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])