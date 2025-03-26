class Password:
    def getPassword(self, user_password: str):
        secure_password = ""
        characters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        length = len(user_password)

        for i in range(length):  
            character = user_password[i]
            index = -1  # Moved index = -1 inside the loop for each character

            for j in range(len(characters)):  
                if characters[j] == character:
                    index = j
                    break  # Added break to exit the loop once the character is found

            if index != -1:  # Only process if character was found
                secure_password += characters[(index + 1) % len(characters)]  # Used modulo to wrap around | the remainder of modulus will be the dividend (index + 1) as it is the remainder

        return secure_password

password = Password()

user_password = str(input("Please enter a password: "))
print(password.getPassword(user_password))

#my version


##class Password:
##    def getPassword(self, user_password: str):
##        secure_password = ""
##        characters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
##        length = len(user_password)
##
##        for i in range(length):
##            character = user_password[i]
##            for i in range(len(characters)):
##                if characters[i] == character:
##                    index = i
##                if index == len(characters):
##                    index = 0
##                secure_password += characters[index + 1]
##        return secure_password
##
##password = Password()
##
##user_password = str(input("Please enter a password: "))
##print(password.getPassword(user_password))
