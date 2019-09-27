#Write a function that provides change directory (cd) function for an abstract file system.
#Notes:
#Root path is '/'.
#Path separator is '/'.
#Parent directory is addressable as '..'.
#Directory names consist only of English alphabet letters (A-Z and a-z).
#The function should support both relative and absolute paths.
#The function will not be passed any invalid paths.
#Do not use built-in path-related functions.
class Path:
    def __init__(self, path):
        self.path = []
        self.cd(path)

    @property#this is the trick to get the 100%
    def current_path(self):
        return '/' + '/'.join(self.path)
        
    def cd(self, new_path):
        if new_path[0] == '/':
            self.path = []
            new_path = new_path[1:]
        
        for i in new_path.split('/'):
            if i == '..':
                self.path.pop()
            else:
                self.path.append(i)
        

path = Path('/a/b/c/d')
path.cd('/x')
print(path.current_path)
