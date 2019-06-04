------ Overview -------------

When designing a Trie we have to take into account structural decisions such as classes, class attributes, instance variables, instance methods, etc., along with time and space complexity. Typically Tries Big O time complexity will be O(M*N)where M is the longest "string" length and N is the total number of strings in the Trie. The key length determines the Trie depth (cite: 1). Space complexity would be O(Key Length * N) where N is number of keys in Trie (cite: 1).

1. insert() and find() - O(M) 
2. suffixes() - O(N)
3. total = O(M)

------- Code Review --------- 

First we declare our `TrieNode` class attributes including a default dictionary from Python to store our child nodes, an `is_word_finished` boolean to confirm our node is the last node of that branch, and a `word_list` list to store our words. 

We will include a __repr__ function for debugging and an `insert()` method which creates a new node to insert. 

Our `suffixes()` class method will take in a prefix parameter and we set current as our self referencing node. Iterating over our current children keys, we check if char in our keys is not present, which we break, add or concat that to our suffix empty string and set current to our new node. 

We call a recursive helper function passing in our current node, and currently created suffix. 

Our `suffixes_recursive` helper method will first check to make sure our node is not at the end, to which we append our suffix to our `word_list` list. Then we iterate over key, and value of our current node's children items and call our `suffixes_recursive` method passing in our value, and our suffix plus or concatenating our key.

For our `Trie` class we declare a `root` attribute referencing `TrieNode` class as a root node. Our `insert()` class method will check if root is None, and if not, set current to root. Now we iterate over the word we will be sending to our Trie. If the letter or char in our word is not in our current node's children, we will add it with a new call to `TrieNode` else, we will set current now to our current node and finally, set `is_word_finished` to True as our iteration thru our Trie brnach is done and word is complete.

The `find()` method will iterate over the prefix passed in and ask if the letter or char in that prefix is one of our current child's nodes. If not, we return None else, we set current to the node that has this char or letter and return that.