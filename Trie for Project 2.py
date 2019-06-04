#%% [markdown]
# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

#%%        
## The Trie itself containing the root node and insert/find functions
from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
            
            for char in word:
                #print('char', char)
                if char not in current.children:                    
                    current.children[char] = TrieNode()
                    #print('cur.child: ', current.children)
                current = current.children[char]
        
            current.is_word_finished = True
            #print('trie', current.children)
    
    def find(self, prefix): # aka key 
        if self.root is None:
            self.root = current
            
        if self.root is not None:
            current = self.root
                        
        for char in prefix:
            #print('char in prefix: ',char)
            if char not in current.children:
                return None    
            current = current.children[char]
            
        return current


#%% [markdown]
# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

#%%
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.is_word_finished = False
        self.children = defaultdict()
        self.word_list = []

    def __str__(self, level = 1):        
        trie = "\t" * level + repr(self.children) + "\n"
        for child in self.children:
            trie += child.__str__() 
        return trie

    def __repr__(self):
        return repr(self.children)

    def insert(self, char):
        self.children[char] = TrieNode()
    
    def suffixes(self, prefix=""): 
        current = self
        suffix = ""
        
        for char in current.children.keys():
            if char not in current.children:
                break
            
            suffix += char
            current = current.children[char] 
        
        self.suffixes_recursive(current, suffix)
        
        for letters in self.word_list:
            print(letters[0:])
        
    def suffixes_recursive(self, current, suffix): 
        if current.is_word_finished:
            self.word_list.append(suffix)
            
        for k, v in current.children.items():
            self.suffixes_recursive(v, suffix + k)

#%% [markdown]
# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

#%%
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


#%%
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')


