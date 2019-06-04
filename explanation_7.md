------ Overview -------------

Designing the Router Trie we have to take into account design decisions such as classes, class attributes, instance variables, instance methods, etc., along with time and space complexity. Typically Tries Big O time complexity will be O(M*N)where M is the longest "string" length and N is the total number of strings in the Trie. The key length determines the Trie depth (cite: 1). Space complexity would be O(Key Length * N) where N is number of keys in Trie (cite: 1).

1. insert() and find() and lookup() - O(M) 
2. total = O(M)

------- Code Review --------- 

First we declare our `RouteTrieNode` class attributes including a default dictionary from Python to store our child nodes and a handler to store our URL handle. 

Our `RouteTrie` class will also have a `handler` denoted by the "/" root slash as in a root directory and a self root referencing a `RouteTrieNode` class storing our root handler. We will include a __repr__ function for debugging and an `insert()` method which our `Router` class will call. Our `insert()` takes in parts of the URL path and our handler name. We iterate over the parts and with an if conditional, ask if our current node's children already has this "part" in their node key. If not, we will set that child's key to a new node else, we will declare current as our newly created node with `item` as its key and finally call current node's handler attribute with the handler parameter. 

The `RouteTrie` class will also have a `find()` method that will iterate over the URL path parts and return the node's handler. Here similarly, we check if that part is in the current node's children. If so, we set current to that node's key else return None. Finally return the current node's handler.

Our `Router` class is called an abstraction layer to our `RouteTrie`. Here in our `Router` attribute we set "root" as a "router" name referencing our `RouteTrie` class passing in our `root_handler`. Our `add_handler()` method will be pivotal to building our Trie as our parameters are the URL path and the handler. We first set router to our current node, which references the `RouteTrie`, and we split the path string. Lastly, we use our `RouteTrie()` `insert()` method to insert the parts of the URL and handler. Our `lookup()` method wil search for a particular path to see if it is present in our Trie, if successfull, returning the deepest leaf's handler. We utilize a `split_path()` helper function to parse our URL path string utilizing Python's `split()` built-in method.


Citations:
1. https://www.geeksforgeeks.org/trie-insert-and-search/