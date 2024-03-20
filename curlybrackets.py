#matching specific repetitions with curly brackets
import re

x=re.compile(r'(Ha){3}')
y=x.search('She laughed HaHaHa yesterday')
print(y.group(),'\n\n')

#python regex are greedy by default ; in ambiguous situations , they will they will match the longest string  possible 
x=re.compile(r'(Ha){3,5}')
y=x.search('She laughed HaHaHaHaHa yesterday')      #greedy regex 
print(y.group())

x=re.compile(r'(Ha){3,5}?')
y=x.search('She laughed HaHaHaHaHa yesterday')      #non-greedy regex
print(y.group())