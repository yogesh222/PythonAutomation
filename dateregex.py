import re

dateregex = re.compile(r'''(
(\d{4})     #year
(-|\.)   #seperator
(\d{2})     #month
(-|\.)   #seperator
(\d{2})     #day
)''',re.VERBOSE)

text = 'My birthdate is 1996-07-27  1996.07.28'
matches = []
for groups in dateregex.findall(text):
    standard = '-'.join([groups[5],groups[3],groups[1]])
    matches.append(standard)
print('\n'.join(matches))
    


    
