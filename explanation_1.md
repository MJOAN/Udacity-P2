------ Overview -------------

Finding the square root of a number can be found by implementing a binary search which takes a low number as 1 and a parameter number as the highest value. From there in our while loop we are calculating a new mid value based on if the mid squared is our number argument. If it is, we return the mid. Otherwise, if mid squared is less than our parameter number, we increase our mid by 1 and assign it to low, while resetting our mid to our result variable. Rather if mid squared is larger than our parameter number, we assign our mid - 1 to high. At each iteration we are dividing our results and iterating until we find our square root.

1. base case if statement - O(1)
2. assigning variables * 3 - O(1) 
3. while loop - O(Log N) 
4. if and if else statements - O(1)
5. total - O(Log N) 

------- Code Review --------- 

We declare a base case if number parameter is equal to zero or 1 we just return the number. We begin a binary search approach with, as our low number is less than or equal to our number parameter. We then declare a mid variable. If our mid index squared happens to be our number, then, great! just return mid. Finally, we use a conditional based on squared mid, if less than our number we set low to mid + 1 and set our square root to our mid else, we set our high to mid - 1. 
