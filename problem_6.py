def get_min_max(l):    
    _min = l[0]
    _max = l[len(l) - 1]
    
    for number in l:
        if l[number] > _max:
            _max = l[number]
        else:
            if l[number] < _min:
                _min = l[number]

    return (_min, _max)

import random
l1 = [i for i in range(0, 9)]  
random.shuffle(l1)

print('Test 1 Randomized List: ', l1)
print('MAX and MIN: ', (max(l1), min(l1)))
print ("Pass" if ((min(l1), max(l1)) == get_min_max(l1)) else "Fail")

l2 = [i for i in range(0, 9)]  
random.shuffle(l2)

print('Test 2 Randomized List: ', l2)
print('MAX and MIN: ', (max(l2), min(l2)))
print ("Pass" if ((min(l2), max(l2)) == get_min_max(l2)) else "Fail")

l3 = [i for i in range(0, 9)]  
random.shuffle(l3)

print('Test 3 Randomized List: ', l3)
print('MAX and MIN: ', (max(l3), min(l3)))
print ("Pass" if ((min(l3), max(l3)) == get_min_max(l3)) else "Fail")