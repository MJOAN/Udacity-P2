------ Overview -------------

Finding the min and max values of a list without using Python's built in `min()` and `max()` functions can be done as an iterative and linary process. We iterate over the list and compare each indexed value to max and min variables set to 0. If the indexed value is less than or greater than our min and max respectively, then we set that indexed value to our min and max. 

Time complexity will be O(N) because of our loop iteration over "N" elements with space complexity as O(1) given the number of "N" elements to store from our array.

1. declare two variables - O(1) * 2
2. for loop - O(N) 
3. if conditionals - O(1) * 2
3. total = O(N)

------- Code Review --------- 
