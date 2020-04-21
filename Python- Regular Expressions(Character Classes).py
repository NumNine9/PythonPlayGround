import re
'''

Character classes provide a way to match only one of a specific set of characters.
a character class is created by putting characters it matches inside square brackets 

pattern =r'[aeiou]'
if re.search(pattern,'grey'):
    print('Match 1')

if re.search(pattern,'qwertyuiop'):
    print('Match 2')

if re.search(pattern,'rhythm myths'):
    print('Match 3')
'''

'''
Character classes also match ranges of characters  
eg.[a-z] matches lowercase aphabetic character
   [0-9] matches any digit number
'''

'''
pattern =r'[A-Z][A-Z][0-9]'
if re.search(pattern,'LSB'):
    print('Match 1')  #only Match 1 is printed

if re.search(pattern,'E3'):
    print('Match 2')

if re.search(pattern,'1ab'):
    print('Match 3')
'''

'''
Place a ^ at the start of a character class to invert it
this causes it to match any character other than the ones included
Other metacharacters such as $ and ., have no meaning within character classes
the metacharacter ^ has no meaning if its not at the beginning
'''
pattern =r'[^A-Z]'
if re.search(pattern,'this is all quiet'):
    print('Match 1')

if re.search(pattern,'AbCfGh123'):
    print('Match 2')

if re.search(pattern,'THISISALLSHOUTING'):
    print('Match 3')
