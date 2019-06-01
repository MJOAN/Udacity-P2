from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict()
    
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self, prefix=""):
        current = self
        word_list = []
        temp = "" 
        print('word_list', word_list)
                
        if current.is_word_finished:
            word_list.append(prefix[:])
        
        for key, value in current.children.items():
            print('cur.child key: ', key, 'val:', value)
            print('curr_child_len', len(current.children.items()))
            temp += key
            word_list.append(temp)
            # self.suffix_recursive(temp)
            print('recursive worked!, word_list: ', word_list)
        
        return word_list
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
            
    def insert(self, word):
        if self.root is None:
            self.root = current
        
        if self.root is not None:
            current = self.root
            
            for char in word:
                print('char', char)
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                print('current', current)
        
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
                if not current.children[char]:
                    return False
                else:
                    node = current.children[char]
                    
            return node

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
    print('prefix', prefix)
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        print('prefixNode: ', prefixNode, type(prefixNode))
        if prefixNode:
            # print('\n'.join(prefixNode.suffixes()))
            print('FINAL!', prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')

# Citations:
# 1. http://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf