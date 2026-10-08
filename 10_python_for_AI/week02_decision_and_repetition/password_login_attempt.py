#Program: Password Login Attempt


password = "Python@=aai"
attempt = 0

while attempt < 3:
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Logged in successfully")
        break
    else:
        print("Please try again") 
        attempt +=1
        

    if attempt == 3:
       print("Maximum login attempts reached. Try again Later.")
       print("Account Locked")