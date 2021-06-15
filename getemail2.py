email_address = input("What is your email address?: ")
import re #import regular expression db
regex = '^[w-.]+@([w-]+.)+[w-]{2,4}$' #symbols and exceptions, tbh I found this string in a forum
def check(email_address):
    if len(email_address) >= 32: #less than 32 char
        print("Invalid Email")
    if len(email_address) <= 2: #more than 2 char
        print("Invalid Email")

    else:
        (re.search(regex, email_address)) 
        print("Thank you, your email address is: " + email_address)
 