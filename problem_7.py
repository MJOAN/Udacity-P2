from collections import defaultdict

class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    def insert(self, part):
        self.children[part] = RouteTrieNode()

    def __repr__(self):
        return str(self.children)+ str(self.children)

class RouteTrie:
    def __init__(self, root_handler = None):
        self.root_handler = "/" 
        self.root = RouteTrieNode(root_handler)  

    def __repr__(self):
        return self.root
    
    def insert(self, parts, handler):
        current = self.root

        for item in parts:
            if item not in current.children:
                current.children[item] = RouteTrieNode(handler)
            current = current.children[item]
            
        current.handler = handler
        
    def find(self, parts):
        if self.root is None:
            self.root = RouteTrieNode()
        else:
            current = self.root

        for item in parts:
            if item not in current.children:
                return None
            else:
                current = current.children[item]
                
        handler = current.handler
        return handler

class Router:
    def __init__(self, root_handler = None):
        self.router = RouteTrie(root_handler)  

    def add_handler(self, path, handler):
        current = self.router
        parts = self.split_path(path)
        current.insert(parts, handler)

    def lookup(self, path):
        current = self.router
        parts = self.split_path(path)
        return current.find(parts)

    def split_path(self, path):
        return path.split("/")[1:]

router = Router("root handler") 
router.add_handler("/", "root handler")
router.add_handler("/home", "home handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/contact", "contact handler")
router.add_handler("/home/applications", "applications handler")
router.add_handler("/home/services", "services handler")
router.add_handler("/home/about/resume", "about resume handler")
router.add_handler("/home/applications/python", "applications python handler")
router.add_handler("/home/services/pricing", "services pricing handler")

print('Test 1: Root path: ', router.lookup("/"))  # root handler
print('Test 1: Home path: ', router.lookup("/home"))  # home handler
print('Test 1: Home about path: ', router.lookup("/home/about"))  # about handler

print('Test 2: Home serivces path: ', router.lookup("/home/services"))   # services handler
print('Test 2: Home applications path: ', router.lookup("/home/applications/python"))   # applications python handler

print('Test 3: Home services pricing path: ', router.lookup("/home/services/pricing"))  # services pricing handler
print('Test 3: Home contact path: ', router.lookup("/home/contact"))  # contact handler

