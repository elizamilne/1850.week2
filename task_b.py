
try: 
    grade = int(input("Input your grade: "))
    if grade>=80 and grade<=100:
        print ("Your grade is: A")
    elif grade>= 60 and grade <= 79:
        print("Your grade is: B")
    elif grade>= 50 and grade<59:
        print("Your grade is: C")
    elif grade>=40 and grade<= 49:
        print("Your grade is: D")
    elif grade >= 0 and grade< 39:
        print("Your grade is: F") 
    elif grade <0 or grade>100:
        print("Error: Grades must be between 0 and 100")
except ValueError:
    print("Error: Please enter a number")