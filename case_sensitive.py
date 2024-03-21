#To make your regex case-insen-
#sitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
import re

x=re.compile(r'RoboCap',re.IGNORECASE)
y=x.search('robocap is a part man, part machine ,all cop')
print(y.group())

#substitute strings with the sub() method
x=re.compile(r'Agent \w+')
y=x.sub('CENSORED','Agent Bob gifted a toy gun to Agent Shaf.')
print(y,'\n')

#say you want to censor the names of the secret agents by
#showing just the first letters of their names. To do this, you could use the
#regex Agent (\w)\w* and pass r'\1****' as the first argument to sub().

x=re.compile(r'Agent (\w)\w*')
y=x.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was adouble agent')
print(y)