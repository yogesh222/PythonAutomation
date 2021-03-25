import re,pyperclip

#phoneRegex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #areacode
    (\s|-|\.)?                          #seperator
    (\d{3})                             #first digit
    (\s|-|\.)                           #seperator
    (\d{4})                             #last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #Extension
    )''',re.VERBOSE)

#EmailRegex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+                       #username
@                                       #@ symbol
[a-zA-Z0-9.-]+                          #domain name
(\.[a-zA-Z]{2,4})                       #dot-something
)''',re.VERBOSE)


#Find matches in clipboard Text
text = str(pyperclip.paste()) #will paste all text from clipboard to text variable
matches = []                  #creates an empty list 
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])  #will put '-' after group 1,3 and 5
    if groups[8] != '':
        phoneNum =+ 'x'+groups[8]
    matches.append(phoneNum)   # will append final matched string to matches list
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # will append groups[0] of matched string 
    
#Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No phone number or email address found ")
    
