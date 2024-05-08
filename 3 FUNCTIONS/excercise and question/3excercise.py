def plaindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return f"{word} is palindrome"
    return f"{word} is not palindrome"

def is_palindrome(word):
    if word == word[::-1]: 
        return True
    return False
#both the function are same


print(plaindrome("oyo"))
print(plaindrome("ayush"))
print(is_palindrome("madam"))