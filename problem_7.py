from collections import defaultdict

class RouteTrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.handler = "home"   
            
    def get_node(self):   
        return RouteTrieNode()     
    
    def insert(self, path):
        self.children[path] = RouteTrieNode()

class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
        self.handler = "/" # root

    def __repr__(self):
        return repr(self)
    
    def insert(self, path):
        if self.root is None:
            self.root = node
        
        if self.root is not None:
            current = self.root
    
        for item in path:
            print('item', item)
            if item not in current.children:
                print('item', item)
                current.children[item] = RouteTrieNode()
            
            current = current.children[item]
            print('curr', current)
        
        print('path: ', path)
        current.handler = path # set final node to full handler ""
            
    def find(self, path):
        if self.root is None:
            self.root = current

        if self.root is not None:
            current = self.root
        
        for char in path:
            print('char in prefix: ',char)
            if char not in current.children:
                return None
            if current.children is None: # we are on the deepest leaf
                print('handler: ', handler)
                handler = current.handler    
        
        print('handler', handler)
        return handler
    
class Router:
    def __init__(self, path):
        self.root = RouteTrie() # for holding routes
    
    def get_node(self):
        return RouteTrieNode()
    
    def add_handler(self, path, handler):        
        parts = self.split_path(path)
        print('parst', parts)
        handler_parts = ""
        
        for part in parts:
            print('parts', part)
            handler_parts += " " + part 
            print('handler_parts: ', handler_parts)
        
        return handler_parts[0:]
                    
    def lookup(self, path):
        current = self.get_node()
        
        parts = self.split_path(path)
        print('parts', parts)
        
        for part in parts:
            if part not in current.children.keys():
                return None
            current = current.children[part]
            
        return current

    def split_path(self, path):
        return path.split("/")        

url_router = RouteTrie()
print(url_router.insert("/home/about"))
print(url_router.insert("/home/contact"))
print(url_router.insert("/home/applications"))
print(url_router.insert("/home/services"))

router = Router("root handler")
print('router', router)

router.add_handler("/home/about", "about handler")  
router.add_handler("/home/contact", "resume handler")  
router.add_handler("/home/applications", "projects handler")  
router.add_handler("/home/services", "contact handler") 

router.add_handler("/home/about/resume", "about resume handler") 
router.add_handler("/home/applications/python", "applications python handler") 
router.add_handler("/home/services/pricing", "services pricing handler") 


print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
