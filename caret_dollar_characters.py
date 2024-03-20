#caret character (^) just after the character class’s opening
#bracket, you can make a negative character class. A negative character class
#will match all the characters that are not in the character class.

import re

x= re.compile(r'[^aeiouAEIOU]')
y=x.findall('Robocop eats baby food.BABY FOOD')
print(y,'\n\n')


#You can also use the caret symbol (^) at the start of a regex to indicate that
#a match must occur at the beginning of the searched text. Likewise, you can
#put a dollar sign ($) at the end of the regex to indicate the string must end
#with this regex pattern. And you can use the ^ and $ together to indicate
#that the entire string must match the regex—that is, it’s not enough for a
#match to be made on some subset of the string.

x=re.compile(r'^Hello')
y=x.search('Hello World')
print(y.group())
print(x.search('He said Hello')==None,'\n\n')

#dollar sign
x=re.compile(r'\d$')
y=x.search('Your number is 42')
print(y.group(),'\n\n')

#both
x=re.compile(r'^\d+$')
y=x.search('3473257')
print(y.group())
