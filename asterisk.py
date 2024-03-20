import re

#matching zero or more with * for the group that precedes the star
x=re.compile(r'Bat(wo)*man')
y=x.search('The adventure of Batman')
print(y.group())

y=x.search('The adventure of Batwoman')
print(y.group())

y=x.search('The Batwowowowoman')
print(y.group(),'\n\n')


#matching one or more with +  ;Unlike the star, which does not require its group to appear in the
#matched string, the group preceding a plus must appear at least once.
x=re.compile(r'Bat(wo)+man')
y=x.search('The adventure of Batwoman')
print(y.group())

y=x.search('The Batwowowowoman')
print(y.group())

