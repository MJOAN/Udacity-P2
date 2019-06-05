------ Overview -------------

Searching a sorted rotated array requires finding a pivot like element to help us know what particular half of our input array to search. A binary search algorithm will be implemented for this problem with slight modification. We will look at our two divided halfs to determine where the array is divided, knowing that each 1/2 will be sorted. Essentially, we implement a mini binary search then on each sorted half. Time complexity for binary search is O(Log N) because of our dividing on each iteration of O(N) and space complexity is O(1) based on how many or "N" elements we have in our array. 

1. declare three variables - O(1) * 2
2. while loop + dividing array in 1/2 iteratively - O(Log N) 
3. total = O(Log N)

------- Code Review --------- 

Searching a sorted rotated array requires finding a pivot element to help us know what particular half of our input array to search. The binary search algorithm will be implemented for this problem with slight modification. We declare a hi and lo variable and begin our while loop, declaring our mid index. If our target value is our mid value then we return our mid. Next steps is where we look at the two divided halfs with additional conditionals. 

First if our mid value is greater than or equal to our lowest value then that means our first half is sorted and so we can begin further exploration. If our target number is less than the mid value that means we need to set our hi to mid - 1 however, in order to proceed our number must also be greater than our lo value. If this is not the case, we move our lo value to mid + 1. 

Next section of our algorithm will be looking at our second half of the input array. If our mid value is less than our highest value, then our second half is sorted. Now we can further explore this section with similar conditionals as above but, reversed. If our target number is greater than our mid and also less than our highest value, then set lo to mid + 1, else, hi to mid - 1. 


Citations:
1. https://www.youtube.com/watch?v=5BI0Rdm9Yhk
2. https://hackernoon.com/fun-with-array-rotations-add4a335d79a
3. https://www.interviewcake.com/concept/java/binary-search