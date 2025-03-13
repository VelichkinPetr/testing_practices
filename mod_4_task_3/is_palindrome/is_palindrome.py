def is_palindrome(s):
    if not isinstance(s,str): raise TypeError
    if s == '': return False
    return s == s[::-1]

