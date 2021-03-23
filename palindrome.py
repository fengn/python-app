import re

def is_palindrome(phase):
    forwards = ''.join(re.findall(r'[a-z]+', phase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
