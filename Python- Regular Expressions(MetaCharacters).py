import re 

'''
Metacharacters are what make regular expressions more powerful than string methods.
They allow you to create regular expressions to represent concepts like 'one or more repetitions of a vowel'
The existence of metacharacters poses a problem if you want to create a regular expression  that,
 matches a literal metacharacter, such as '$'. You can do this by putting a backslash in front of them.
 However, this can cause problems, since backslashes also have an escaping function in Python strings.
 This can mean putting 3 or 4 backslashes in a row to do all the escaping.

The Dot ( . )


pattern =r'gr.y'
if re.match(pattern,'grey'):
    print('Match 1')

if re.match(pattern,'gray'):
    print('Match 2')

if re.match(pattern,'blue'):
    print('Match 3')
'''

# the next two metacharacters are ^ and $
pattern =r'^gr.y$'
if re.match(pattern,'grey'):
    print('Match 1')

if re.match(pattern,'gray'):
    print('Match 2')

if re.match(pattern,'stingray'):
    print('Match 3')
