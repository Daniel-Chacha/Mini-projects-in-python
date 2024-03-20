#program to find a phone number from a line(s) od text as well as text if a sting is phone number
def isphoneNumber(text):
    if len(text)!=12:
        return False
    for x in range(0,3):
        if  not text[x].isdecimal():
            return False
        
    if text[3]!='-':
        return False
    
    for x in range(4,7):
        if not text[x].isdecimal():
            return False
        
    if text[7]!='-':
        return False
    for x in range(8,12):
        if not text[x].isdecimal():
            return False
    #print(text,'is a phone number')
    return True

#print(isphoneNumber('412-234-4355'))
#print(isphoneNumber('mezandogoizoo'))

#print phone number from a line of text
message='Call me at 1500 hours tomorrow via 234-342-8945. To reach my office use 345-129-9834.'
for x in range(len(message)):
    chunk=message[x:x+12]
    if isphoneNumber(chunk):
        print('Phone number found: ',chunk)
