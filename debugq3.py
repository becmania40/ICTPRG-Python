# A time traveler has suddenly appeared in your classroom!
# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) #extra parenthesis needed at int

if year <= 1980:
    print('Woah, that is the past!') #two different quotation marks
elif year >= 1980 & year <= 2020: #two & added =
    print("That is totally the present!") #debugger hated the ' 
elif year >= 2021: #add definition
    print("Far out, that is the future!!")