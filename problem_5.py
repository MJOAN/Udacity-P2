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
            if not current.children[char]:
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
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
            
            for char in word:
                # print('char', char)
                if char not in current.children:                    
                    current.children[char] = TrieNode()
                    # print('cur.child: ', current.children)
                current = current.children[char]
        
            current.is_word_finished = True
            print('trie', current.children)
    
    def find(self, prefix): 
        if self.root is None:
            self.root = current
            
        if self.root is not None:
            current = self.root
                        
        for char in prefix:
            # print('char in prefix: ',char)
            if char not in current.children:
                return None    
            current = current.children[char]
            
        return current

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

MyTrie = Trie()
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        # print('prefixNode: ', prefixNode)
        if prefixNode:
            print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print(str(MyTrie))
        print('')
interact(f,prefix='')

# Citations:
# 1. http://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf
# 2. http://www.cs.cmu.edu/afs/cs/academic/class/15451-f17/www/lectures/lec10-sufftree.pdf
# 3. https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014 
# 4. https://www.hackerearth.com/practice/data-structures/advanced-data-structures/suffix-trees/tutorial/
# 5. https://startupnextdoor.com/fun-with-tries/
