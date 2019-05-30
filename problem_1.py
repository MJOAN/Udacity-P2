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

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Citations: 
# 1. https://www.geeksforgeeks.org/square-root-of-an-integer/
