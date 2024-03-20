import re

x=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
y=x.search('my number is 245-456-3454 ')
print('Phone Number found: ',y.group(),'\n')


#alternatively
x=re.compile(r'\d{3}-\d{3}-\d{4}')
y=x.search('my number is 245-456-3454 ')
print('Phone Number found: ',y.group(),'\n\n')

#grouping with parenthesis
x=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
y=x.search('my number is 245-456-3454 and 456-764-0933')
print(y.group())
print(y.group(0))
print(y.group(1))
print(y.group(2))
print(y.groups(),'\n\n')

z=x.findall('my number is 245-456-3454 and 456-764-0933')
print(z,'\n\n')

#since the groups() method returns a tuple, we can assign the values to variables
areacode,mainnumber=y.groups()
print(areacode)
print(mainnumber,'\n\n')


#at times , the area code may be encapsulated in brackets, to encompass this change, the brackets need to be escaped

x=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
y=x.search('my number is (245) 456-3454 ')
print(y.group())
print(y.group(0))
print(y.group(1))
print(y.group(2))
print(y.groups(),'\n\n')


#findall in groups
x=re.compile(r'(\d\d\d)(-\d\d\d)(-\d\d\d\d)')
y=x.findall('my number is 245-456-3454 and 456-764-0933')
print(y)