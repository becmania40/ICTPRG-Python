def is_odd(number):
    if (number % 2) != 0:
        status=True
    else:
        status=False
    return status

#print( is_odd(2))
#print( is_odd(3))
#print( is_odd(4))
#print( is_odd(5))

num = int(input("Enter a number: "))
if is_odd(num):
    print("The number is odd")
else:
    print("The number is even")