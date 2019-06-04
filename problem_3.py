def rearrange_digits(l):
    l = mergesort(l) 
    
    first_max_sum = 0
    second_max_sum = 0
    
    for number in range(len(l)):  # cite: 1
        if (number % 2 == 0): 
            first_max_sum = first_max_sum * 10 + l[number] # cite: 4
        else:
            second_max_sum = second_max_sum * 10 + l[number]
       
    return [first_max_sum, second_max_sum]

def mergesort(items): # cite: 2

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)

def merge(left, right):
    
    merged = []
    left_index = 0 
    right_index = 0
       
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]: # for reverse order
            merged.append(left[left_index]) 
            left_index += 1
        else:
            merged.append(right[right_index]) 
            right_index += 1
    
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged
    
def test_function1(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print('output_mine: ', output)
    print('solution_test: ', solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_function1([[1, 2, 3, 4, 5], [542, 31]]) 
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]

    
def test_function2(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print('output_mine: ', output)
    print('solution_test: ', solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_function2([[1, 2, 3, 4, 5], [542, 31]]) 
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]


    
def test_function3(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print('output_mine: ', output)
    print('solution_test: ', solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_function3([[1, 2, 3, 4, 5], [542, 31]]) 
test_case3 = [[4, 6, 2, 5, 9, 8], [964, 852]]





# Citations:
# 1. https://www.geeksforgeeks.org/sum-even-odd-elements-array/
# 2. http://localhost:8888/notebooks/Notebooks/Udacity/merge_sort_walkthrough.ipynb
# 3. https://stackoverflow.com/questions/49618039/how-can-i-re-sort-an-array-in-place-to-put-the-even-indexed-items-before-the-odd
# 4. https://stackoverflow.com/questions/33607753/way-to-combine-integer-array-to-a-single-integer-variable