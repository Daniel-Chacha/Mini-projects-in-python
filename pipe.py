# the pipe character | is used in matching
#the first occurrence is returned

import re
x=re.compile(r'Batman|Fay')
y=x.search('Batman and together with Fay are here')
print(y.group(),'\n\n')

#also used to match one of several patterns
x=re.compile(r'Bat(man|mobile|copter|bat)')
y=x.search('A person named Batmobile was here')
print(y.group())
print(y.group(1),'\n\n')

#optional matching with the question mark  ; would as well return Batman if found
x=re.compile(r'Bat(wo)?man')
y=x.search('I heard Batwoman is out')
print(y.group())
y=x.search('I heard Batman is out')
print(y.group(),'\n\n')

#look for phone numbers with area codes as well as those that do not have
x=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
y=x.search('She gave him the number 345-566-0790 ')
print(y.group())
y=x.search('She gave him the number 566-0790 ')
print(y.group(),'\n\n')


