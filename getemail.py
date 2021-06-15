email_address = input("What is your email address?: ")
while "@" not in email_address:
    email_address = input("Your email is missing the '@' symbol\nPlease write your email again: ")
    if len(email_address) <= 2:
        email_address = input("Your email is too short\nPlease write your email again: ")
    if len(email_address) >= 32:
        email_address = input("Your email is too long\nPlease write your email again: ")
    if "." not in email_address:
        email_address = input("Your email must have '.' in it\nPlease write your email again: ")
else:
    print('Thank you, your email address is: '+ email_address)
while "." not in email_address:
    email_address = input("Your email must have '.' in it\nPlease write your email again: ")
    if len(email_address) <= 2:
        email_address = input("Your email is too short\nPlease write your email again: ")
    if len(email_address) <= 32:
        email_address = input("Your email is too long\nPlease write your email again: ")
    if "@" not in email_address:
        email_address = input("Your email is missing the '@' symbol\nPlease write your email address again: ")