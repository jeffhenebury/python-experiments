### Name: Jeff Henebury
###Date: 10/12/21
### Purpose:
# '''Program for password-saving into a file.
# Added functionality:
# 1. Have added a 'password strength-checker' via my passwordOkay function. When adding a new password,
# the program will check to make sure that the submitted password meets the following security criteria:
#   a) at least 8 characters long,
#   b) consists of more than just letters (has to also have numbers and/or symbols
#   c) Does not contain obvious passwords like 'password1'
#   d) Is a unique password that has not been re-used from a previous saved password.
# 2. Have added a 'password deleter' so that previously added passwords can be removed. The
#   passwordeleter function then calls savePasswordFile in order to save the changes.
#
# I've left my comments in for now to show steps taken etc. Thanks!
#  '''


import csv
import sys


passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]

passwordFileName = "samplePasswordFile"

encryptionKey = 16


def passwordRepeatChecker(passwordSubmission):
    for lsts in passwords:
        if passwordEncrypt(passwordSubmission, encryptionKey) == lsts[1]:
            return True
    return False


##Trying to add a password checker that will make sure the user is excercising good password hygeine.
def passwordOkay(passwordSubmission):
    if passwordSubmission.isalpha():  # anything that doesn't have numbers in the password
        print('Password cannot contain only letters: please add numbers and/or symbols')
        return False
    # eliminating very common and bad passwords
    elif passwordSubmission.lower() == ('password', 'Password1', 'ABCD1234'):
        print('Too obvious a password.'
              'Please choose something less easy to guess!')
        return False
    elif len(passwordSubmission) < 8:
        print('Password is not long enough. '
              'Password must be 8 characters or longer.')
        return False
    # elif passwordEncrypt(passwordSubmission, 16) in passwords:
    elif passwordRepeatChecker(passwordSubmission):
        print('You have already used the password ' + passwordSubmission +
              ' on another site. Please choose a unique password.')
        return False
    else:  # if it meets the above requirements, it is good!
        return True


# password deleter
def passwordDeleter(website):
    for i in range(len(passwords)):
        if website == passwords[i][0]:
            passwords.pop(i)
            print(website + ' has been deleted from the saved passwords list.')
            savePasswordFile(passwords, passwordFileName)
            return
    # if no website matches input, print an error message, go back to home screen
    print(
        website + ' is not a website for which you have a saved password.')


# Caesar Cypher Encryption
def passwordEncrypt(unencryptedMessage, key):
    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage, add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        #if it's not a number, just add it as is for now
        else:
            encryptedMessage += symbol

    return encryptedMessage


# Caesar Cypher decrypter
def passwordDecrypt(encryptedMessage, key):
    #start with an empty string as our decryptedMessage
    decryptedMessage = ''

    # For each symbol in the unencryptedMessage, add an encrypted symbol into the encryptedMessage
    for symbol in encryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            decryptedMessage += chr(num)
        else:
            decryptedMessage += symbol
    return decryptedMessage


def loadPasswordFile(fileName):
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Bonus option! Delete a password from your saved list.")
    print(" 6. Print the encrypted password list (for testing")
    print(" 7. Quit program.")
    print("Please enter a number (1-7)")
    choice = input()

    if (choice == '1'):  # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if (choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):
            #     print("TEST, what does this print out? " + str(i) + " " + passwords[i][0])
            if passwords[i][0].lower() == passwordToLookup.lower():
                # print("TEST: " + passwordToLookup + " IS in your list at position:" + str(i))
                print("The encrypted password for " + passwordToLookup + " is: " + passwords[i][1])
                # how to unencrypt the password:
                correctEncryptedPassword = passwords[i][1]
                print('The decrypted password is = ' + passwordDecrypt(correctEncryptedPassword, encryptionKey))
            else:
                continue
        #      print("TEST: " + passwordToLookup + " IS NOT in your password saved list. Please try again.")



    if (choice == '3'):
        print("What website is this password for?")
        website = input()
        ###Adding functionality: doing a 'password check' to make sure it is a strong password
        while True:
            print("What is the password?")
            unencryptedPassword = input()
            if passwordOkay(unencryptedPassword):
                print('Acceptable password! That has been saved.')
                break
            else:
                print(
                    "I am sorry, that password does not meet the minimum security requirements for the above-listed reason.")
                print('''Please make sure your password is: 
                1. At least 8 characters long
                2. Contains letters AND numbers/ symbols (not just letters)
                3. Is not something super obvious like "Password1."
                4. Is not a password you have previously used on another site.''')


        # encrypt the password and store it in the list of passwords

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        newList = [website, encryptedPassword]
        passwords.append(newList)


    if (choice == '4'):  # Save the passwords to a file
        savePasswordFile(passwords, passwordFileName)

    if (choice == '5'):  # deletes a saved password from the list
        print("What website would you like to delete the password for?")
        website = input()
        passwordDeleter(website)

    if (choice == '6'):  # print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))
        #### adding iteration through a list test
        # print('TEST: iterating through all elements in a list')
        # for word in passwords:
        #    print(word)
        #    print(word[1])

    if (choice == '7'):  # quit the program
        sys.exit()

    print()
    print()
