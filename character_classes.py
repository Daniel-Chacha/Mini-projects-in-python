#at times shorthand character classes are too broad. you can define your own classes
import re

x= re.compile(r'[aeiouAEIOU]')
y=x.findall('Robocop eats baby food.BABY FOOD')
print(y)

#include ranges of letters and numbers   ;;;insidethe square brackets , you do not need to escape the .,@#*
x=re.compile(r'[a-zA-Z0-9]')
y=x.findall('He said that he was 27 years old.')
print(y)
