while True:
    asknumber = input('Please input correct number to continue: ')
    validnum = '5' #definte number
    if asknumber == validnum: #define point of the program
        print('Correct, you entered: ' + asknumber)
        break
    else:
        print('Incorrect')
        continue