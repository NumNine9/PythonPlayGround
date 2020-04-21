import re

pattern = r'spam'
if re.match(pattern,'spamspamspam'):
    print('Match')
else:
    print('No match')

'''
Regular expressions used for string manipulations 
-->verifying for string patterns
-->performing substitutions in a string
They are a domain specific language (DSL)
Regular expressions can be accessed using the 're' module
the 're.match' function can be used to determine whether it matches at the beginning of a string 
other functions to match patterns are 're.search' and 're.findall'
the 're.search finds a match of a pattern anywhere in a string
the 're.findall' returns a list of all substrings that match a pattern
'''

pattern= r'spam'
if re.search(pattern,'eggspameggspameggspam'):
    print('Match')
else:
    print('No match')
if re.match(pattern,'eggspameggspameggspam'):  #it only looks at the beginning of the string
    print('Match')
else:
    print('No match')

print(re.findall(pattern,'eggspameggspameggspam'))

"""
The Regex search returns an object with several methods that give details about it 
These methods include group which returns the string matched,
start and ending positions of the first match, and span which returns the start and end positions of the match as a tuple
"""
pattern = r'pam'
match= re.search(pattern,'eggspameggspameggspam')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

