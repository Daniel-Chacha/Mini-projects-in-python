#from a many lines of text, find phone numbers and emails

import re,pyperclip

text=str(pyperclip.paste())

phonenumber=re.compile(r"""
(\d{3}|\(\d{3}\))?       #area code
(\s|-|\.)?               #separator
(\d{3})                 #three digit 
(\s|-|\.)               #separator
(\d{4})                 #last four digit       
(\s*(x|ext|ext.)\s*\d{2,5})?   #extension
                                                                                                                   
                       
""",re.VERBOSE)

email=re.compile(r'''(
[a-zA-Z0-9._%+-]+
[@]
[a-z]+
[.]                 
[a-zA-Z]{2,4}                                                                  

)''',re.VERBOSE)

matches=[]
    
for m in email.findall(text):
#for groups in phonenumber.findall('my numbers are 123-122-3324 and (456) 345 4568 and (789)-546-7686ext234'):
    #print(groups)
    phoneNum=','.join(list(groups))
    #print(phoneNum)
    phoneNum1=phoneNum.replace(",","")
    #if len(phoneNum1)<14:
        #matches.append(phoneNum1)

    #if len(phoneNum1) >19:
        #if len(phoneNum1) <21:
            #phoneNum2=phoneNum1.removesuffix('x')
            #matches.append(phoneNum2)
        #elif len(phoneNum1) <24:
            #phoneNum2=phoneNum1.removesuffix('ext')
            #phoneNum1=phoneNum2
            #matches.append(phoneNum2)
        #elif len(phoneNum1) <26:
            #phoneNum2=phoneNum1.removesuffix('ext.')
            #matches.append(phoneNum2)


    matches.append(phoneNum1)
    
    
for m in email.findall(text):
 
#for m in email.findall(' my emails are : danmwita355@gmail.com , dmwita455@gmail.com and smwita42@yahoo.com'):
    matches.append(m)
    

print(matches)
pyperclip.copy(str(matches))
#for x in range(len(matches)):
    #print(matches[x])

#if len(matches)>0:
 #   pyperclip.copy('\n'.join(matches))
  #  print('copied to clipboard')
    #print('\n'.join(matches))
#else:
 #   print('No phone numbers or email addresses  found')
#print(pyperclip.paste())
