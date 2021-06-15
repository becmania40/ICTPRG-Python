#import sys
wordlist = input('Tell me something good, but only in a few words!')
if len(wordlist)>6:
    print('Nah that is too long, try again')
if len(wordlist)<4:
    print('No that is not long enough, cmon!')
if wordlist == 4:
    print('Ah that is nice')