def is_palindrome(word):
    word = word.lower().replace(" ", "")
    reversed_word = word[::-1]

    if word == reversed_word:
        return True
    else:
        return False