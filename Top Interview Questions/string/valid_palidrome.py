import re

def valid_palidrome(s):
    s = s.lower()
    s = ''.join([c if c.isalnum() else '' for c in s])
    return s[::-1] == s

print(valid_palidrome("A man, a plan, a canal: Panama"))
