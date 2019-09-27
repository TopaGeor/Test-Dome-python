#4. Palindrome

def is_palindrome(word):
    s = len(word)
    if(s%2 == 1):
        y = word[:s//2]
        x = word[:s//2:-1]
        if(x.lower() == y.lower()):
            return True
    else:
        y = word[:s//2]
        x = word[:s//2 - 1:-1]
        if(x.lower() == y.lower()):
            return True
    return None
    
print(is_palindrome('Deleeled'))