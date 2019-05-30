# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum. 
# Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
# The number of digits in both the numbers cannot differ by more than 1. 
# You're not allowed to use any sorting function that 
# Python provides and the expected time complexity is O(nlog(n)).

def rearrange_digits(input_list):
    lo = 0
    hi = len(input_list) - 1
    current_maximum = 0
    highest_maximum = 0
    
    while lo <= hi:
        mid = (lo + hi)//2
        
        first_half = input_list[:mid]
        second_half = input_list[mid:]
        
        print('first1/2', first_half)
        print('second1/2', second_half)
        
        left = list_to_numbers(first_half)
        right = list_to_numbers(second_half)
        
        print('left: ', left)
        print('right: ', right)
        
        current_maximum = right + left 
        print('current_maximum', current_maximum)
        
        if left + right > current_maximum:
            highest_maximum = current_maximum
            print('highest_maximum', highest_maximum)
            hi -= 1
            continue
        else: 
            lo += 1
            continue
        
    print('final', left, right)
    return (left, right)
        
def list_to_numbers(_list): # cite: 1
    numbers = [str(i) for i in _list]
    result = int("".join(numbers))
    return result
        
    # divide list into two halfs using a pivot 
    # merge sort similar
    # add each half of list as one whole number
    # set maximum variable 
    # if convert list 1 to numbers as (sum) + 
    # convert list 2 to numbers as (sum) 
    # add both as current max
    # if current max is greater than highest max then,
    # update maximum 
    # return max 

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) 
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]] 

# Citations:
# 1. https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/
