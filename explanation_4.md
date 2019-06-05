------ Overview -------------

Separating 0s, 1s, and 2s, from an unsorted array of said values requires a partitioning type of approach like quicksort but, implemented using principles from binary search with lo and hi to target mid values which we either increment or decrement based on the mid value. 

-- If a mid value is 0 then we swap lo and mid moving them toward the LEFT side of the 1s group and incrementing both pointers.

-- Continuing on, if mid value is 2 then we swap mid and hi values toward the RIGHT side of the 1s and decrement hi value. Finally all else, we just increment mid by 1. 

-- Once mid's value has surpassed hi's value we end the while loop and return the final segregated list of 0s, 1s and 2s in proper order.

Time complexity will be O(N) because of our loop iteration over "N" elements with space complexity as O(1) given the number of "N" elements to store from our array.

1. assign three variables - O(1) * 3
2. while loop - O(N) 
3. if conditionals and swaps - O(1) * 7
4. total - O(N)

