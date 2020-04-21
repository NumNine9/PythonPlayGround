'''
one of the most important 're' methods are that use regular expressions is sub

syntax:   re.sub(pattern,repl,string,count=0)

this method replaces all occurrences of the pattern in string with repl, substituting all occurences, 
unless count provided. This method returns the modified string 
'''
import re 

text = 'My name is George. Hi George.'
pattern = r'George'
newtext= re.sub(pattern, 'Amy',text)
print(newtext)