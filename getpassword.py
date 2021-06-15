import re
password = input("Please select a password: ")
flag = 0
while True:  
    
    if (len(password)<8): #length min 7
        flag = -1
        break
    elif re.search("[password]", password): #don't allow the word password
        flag = -2
        break
    elif not re.search("[a-z]", password): #lowercase
        flag = -1
        break
    elif not re.search("[A-Z]", password): #uppercase
        flag = -1
        break
    elif not re.search("[0-9]", password): #inc number
        flag = -1
        break
    elif not re.search("[_*&^%#@$!]", password): #inc symbol
        flag = -1
        break
    else:
        flag = 0
        print("Thank you, valid password")
        break
if flag == -1: #identify lack of symbol, len etc
    print("Try again making sure you use a symbol, number and mix of capital and lowercase letters and more than 7 characters.")
if flag == -2: #identify password flag
    print("Your password cannot contain the word 'password'")