def convert(string):
    li = list(string.split(' '))
    return li


def is_palindrome(str_):
    s = convert(str_)
    if s[::1] == s[::-1]:
        return True
    return False


str1 = str(input('Enter the sentence: '))
print(is_palindrome(str1))
