password= input(" Input a password \n Passwords must contain both numbers and letters  and be more than 8 charcahters\n")

length = False
num= False

if len(password)>8:
    for char in password:
        if char.isalpha():
            length= True
        if char.isdigit():
            num= True
    

if length and num :
    print("Your password is valid")
elif num  and not length :
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
elif not num and length:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
