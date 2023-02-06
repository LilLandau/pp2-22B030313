def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word)-1-i]:
            return False
    
    return True