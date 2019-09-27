#4. Palindrome
#A palindrome is a word that reads the same backward or forward.
#Write a function that checks if a given word is a palindrome. Character case should be ignored.
#For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled",
#which is a palindrome since it reads the same backward and forward.

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
