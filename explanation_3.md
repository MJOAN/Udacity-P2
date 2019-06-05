------ Overview -------------

Finding max and min of an array requires declaring two variables for max and min which are the last element and first element respectively. 

We will iterate thru the list of values comparing the max to the list element. If the list element is greater than max then set max to that element. Else, if list element is less than min value, we set min to that list element value. After iteration completes we return both max and min. Time complexity will be O(N) because of our loop iteration over "N" elements with space complexity as O(1) given the number of "N" elements to store from our array.

1. declare two variables - O(1) * 2
2. for loop over list - O(N)
3. if statements check for max, min - O(1) * 2
4. total - O(N)
