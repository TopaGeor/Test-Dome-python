class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        if new_path[0] == '/':
            self.current_path = ''
        
        np = new_path.split('/')
        cp = self.current_path.split('/')
        for i in np:
            if i == '..':
                cp = cp[:len(cp)-1]
            elif(i >= 'a')and(i <= 'z'):
                cp.append(i)
            elif(i >= 'A')and(i <= 'Z'):                
                cp.append(i)
            else:
                print("invalid path")
                return 
                
                    
        update = ''
        for i in cp[1:]:
            update += '/'
            update += i
        
        self.current_path = update
        

path = Path('/a/b/c/d')
path.cd('/..')
print(path.current_path)

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        if new_path[0] == '/':
            self.current_path = ''
            new_path = new_path[1:]
        
        cp = self.current_path.split('/')
        
        for i in new_path.split('/'):
            if i == '..':
                cp.pop()
            else:
                cp.append(i)
 
        
        self.current_path = '/'.join(cp)
        

path = Path('/a/b/c/d')
path.cd('x/a/d')
print(path.current_path)

class Path:
    def __init__(self, path):
        self.dirs = []
        self.cd(path)

    @property
    def current_path(self):
        return '/' + '/'.join(self.dirs)
        
    def cd(self, new_path):
        if new_path[0] == '/':
            self.dirs = []
            new_path = new_path[1:]
        
        for i in new_path.split('/'):
            if i == '..':
                self.dirs.pop()
            else:
                self.dirs.append(i)
        

path = Path('/a/b/c/d')
path.cd('/x')
print(path.current_path)