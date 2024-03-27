#program to check whether password entered is strong enough
import re

password='a2!Saaaaaaa'

pass_char1=re.compile(r'(a-z)*')
pass_char2=re.compile(r'(A-Z)*')
pass_char3=re.compile(r'(0-9)*')
pass_char4=re.compile(r'[!@#$%^&*()_+?><|":}{]*')

if len(password) <8:
    print('A strong password should be at least 8 characters')
else:
    try:
        if (pass_char1.search(password)==None) ==True:
            if pass_char2.search(password) ==True:
                if pass_char3.search(password) ==True:
                    if pass_char4.search(password) ==True:
                        print('Strong password set')
                    else:
                        print('A strong password should also  contain symbols')
                else:
                    print('A strong password should also contain numbers and symbols')
            else:
                print('A strong password should also contain uppercase letters,lowercase letters,numbers and symbols')
        else:
            print('A strong password should also contain Uppercase letters,lowercase letters,numbers,  and symbols')
    except:
        print('A strong password should contain uppercase letters,lowercase letters,numbers and symbols')

print(pass_char1.search(password)==None)
print(pass_char2.search(password)==None)
print(pass_char3.search(password)==None)
print(pass_char4.search(password)==None)
print(pass_char1.search('aaaaaaaa').group())