day = input("Enter a day of the week: ")
day = day.capitalize()


match day:
    case "Monday":
        print("Monday is day 1")
    case "Tuesday":
        print("Tuesday is day 2")
    case "Wednesday":
        print ("Wednesday is day 3")
    case "Thursday":
        print ("Thursday is day 4 ")
    case "Friday":
        print ("Friday is day 5 ")
    case "Saturday":
        print ("Saturday is day 6 ")
    case "Sunday":
        print ("Sunday is day 7 ")
    case _:
        print ("Please enter a valid day.")