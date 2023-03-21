# Naiya Rampat

def encode(password):
    # creates variable for the new password
    new_password = []
    # for loop tp add 3 to each digit in the password
    for num in password:
        num = int(num)
        num += 3
        # stores updated password values to new list
        new_password.append(num)
    # creates a variable for the new password
    final_password = ""
    # for loop to add the new values of each digit to the new password string
    for num in new_password:
        final_password += str(num)
    # returns new password
    return final_password

def decode(password):
    new_password = []
    for num in password:
        num = int(num)
        num -= 3d
        new_password.append(num)
    final_password = ""
    for num in new_password:
        final_password += str(num)
    return final_password


encoded_password = " "
if __name__ == "__main__":
    # while loop to continue to print the options while true
    while True:
        # prints the menu and allows for user to input the option
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            # option to encode the password
            # input the original password
            user_password = input("Please enter your password to encode:")
            # set the encoded password to the password once it runs though the encode function
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        if option == 2:
            dec= decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {dec} ")
        if option == 3:
            # quits the program
            break
