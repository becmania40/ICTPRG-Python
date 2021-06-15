grade = int(input("What was your score?"))
if  grade < 69 and grade > 50:
    print("Congrats, you barely passed")
elif grade < 79 and grade > 70:
    print("Cool, Credit!")       
elif grade < 89 and grade > 80:
    print("Awesome, Distinction!")   
elif grade > 90:
    print("Well done, smarty pants! Here is your High Distinction")             
else:
    print("You failed the test!")    