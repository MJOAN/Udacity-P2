from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict()
        self.key = None
    
    def add(self, char):
        if self is None:
            self.children[char] = TrieNode()
            
        if self is not None:
            self.children[char]
    
    def suffixes(self, suffix=""):       
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
              
        for char in suffix:
            if char not in current.children:
                return False
            else:
                current = current[char]
        
        if current is not None and '$' in current:
            return current
                    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def build_suffixes(self, word):
        word += '$' 
        
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
        
        for i in range(len(word)):
            for char in word[i:]:
                if char not in current.children:
                    print('char', char)
                    current.children = defaultdict()
                else:
                    current = current[char]
                    print('current', current)
            
    def insert(self, word):
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
            
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
        
        current.is_word = True
        print('trie', current.children)
    
    def find(self, prefix): # aka key 
        if self.root is None:
            self.root = current
            
        if self.root is not None:
            current = self.root
                        
        for char in prefix:
            print('char in prefix: ',char)
            for child in current.children:
                print('child in curr children: ', child)
                if child != char:
                    continue
                elif child == char:
                    return True
                else:
                    return False

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
                
MySuffixTrie = Trie()
for word in wordList:
    MySuffixTrie.build_suffixes(word)
    print('MySuffixTrie', MySuffixTrie)
            
MyTrie = Trie()
for word in wordList:
    MyTrie.insert(word)
    
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    print('prefix', prefix)
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        print('prefixNode: ', prefixNode)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')

# Cite: http://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf