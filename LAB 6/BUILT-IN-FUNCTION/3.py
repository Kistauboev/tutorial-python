def isPalindrome(string):
    reverse = string.upper()[::-1]
    return reverse == string.upper()

string = input()
print(isPalindrome(string))