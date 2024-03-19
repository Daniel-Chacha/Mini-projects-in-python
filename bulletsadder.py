#get a string of text from the clipboard and add bullets at the start of each line,split and the copy it back to the clipboard 

import pyperclip

text=pyperclip.paste()
lines=text.split('\n')
#print(lines)
for x in range(len(lines)):
    lines[x]='*' +lines[x]

text='\n'.join(lines)
#print(text)
pyperclip.copy(text)
#print(pyperclip.copy(text))

