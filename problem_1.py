def sqrt(number):
    if(number == 0) or (number == 1):
        return number
    
    square_root = 0
    low = 1
    high = number
    
    while (low <= high): # cite: 1
        mid = (low + high) // 2
        
        if (mid * mid == number):
            return mid
        
        if (mid * mid < number):
            low = mid + 1
            square_root = mid
        else: 
            high = mid - 1

    return square_root  

print ("Test 1 Pass" if  (3 == sqrt(9)) else "Fail")
print ("Test 1 Pass" if  (0 == sqrt(0)) else "Fail")
print ("Test 1 Pass" if  (4 == sqrt(16)) else "Fail")
print ("Test 1 Pass" if  (1 == sqrt(1)) else "Fail")

print ("Test 2 Pass" if  (2 == sqrt(4)) else "Fail")
print ("Test 2 Pass" if  (6 == sqrt(36)) else "Fail")
print ("Test 2 Pass" if  (7 == sqrt(49)) else "Fail")

print ("Test 2 Pass" if  (9 == sqrt(81)) else "Fail")
print ("Test 2 Pass" if  (12 == sqrt(144)) else "Fail")
print ("Test 3 Pass" if  (13 == sqrt(169)) else "Fail")
print ("Test 3 Pass" if  (10 == sqrt(100)) else "Fail")


# Citations: 
# 1. https://www.youtube.com/watch?v=plbSgfLCt74
# 2. https://helloacm.com/binary-search-sqrt/ 