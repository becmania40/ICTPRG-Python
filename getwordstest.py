import re
#re.findall(string,flags=0)
wordlist = input('Tell me something good, but only in a few words!: ')
if input.count(wordlist)>6:
    print('try again, too long')
if input.count(wordlist)<4:
    print('try again, too short')
else:
    print('Cool, that IS good.')