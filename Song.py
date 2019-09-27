#Song
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        dic = {}
        next = self.next
        name = self.name
        while (next!=None):
            if(name not in dic):
                dic[name] = next
                name = next
                next = next.next
            else:
                return True
        
        return False            

            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())