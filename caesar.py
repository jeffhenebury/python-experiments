#shift letters by the number provided, start with constants
chosenLet = input('what letter to start with?')
advancer = int(input('How much to shift by?'))


def numberShrinker(x):
    x = int(x)
    while (x > 26):
        x = x % 26
        print('After division by 26, remainder is : ' + str(x))
    return x

def letterToNum(x):
    x = str(x)
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case 'c':
            return 3
        case 'd':
            return 4
        case 'e':
            return 5
        case 'f':
            return 6
        case 'g':
            return 7
        case 'h':
            return 8
        case 'i':
            return 9
        case 'j':
            return 10
        case 'k':
            return 11
        case 'l':
            return 12
        case 'm':
            return 13
        case 'n':
            return 14
        case 'o':
            return 15
        case 'p':
            return 16
        case 'q':
            return 17
        case 'r':
            return 18
        case 's':
            return 19
        case 't':
            return 20
        case 'u':
            return 21
        case 'v':
            return 22
        case 'w':
            return 23
        case 'x':
            return 24
        case 'y':
            return 25
        case 'z':
            return 26
        case _:
            return 0  # 0 is the default case if x is not found

def advanceNum(x, advancer):
    x = int(x)
    x += int(advancer)
    return x

def numberToLetter(num):
    match num:
        case 1:
            return 'a'
        case 2:
            return 'b'
        case 3:
            return 'c'
        case 4:
            return 'd'
        case 5:
            return 'e'
        case 6:
            return 'f'
        case 7:
            return 'g'
        case 8:
            return 'h'
        case 9:
            return 'i'
        case 10:
            return 'j'
        case 11:
            return 'k'
        case 12:
            return 'l'
        case 13:
            return 'm'
        case 14:
            return 'n'
        case 15:
            return 'o'
        case 16:
            return 'p'
        case 17:
            return 'q'
        case 18:
            return 'r'
        case 19:
            return 's'
        case 20:
            return 't'
        case 21:
            return 'u'
        case 22:
            return 'v'
        case 23:
            return 'w'
        case 24:
            return 'x'
        case 25:
            return 'y'
        case 26:
            return 'z'
        case _:
            return 0  # 0 is the default case if x is not found

def multiCypher (word):
    decrypted:''
    for letter in word:
        lowerChosen = chosenLet.letter()


#print(lowerChosen)

 #make it lower case
lowerChosen = chosenLet.lower()
#strip down if above 26
advancer = numberShrinker(advancer)
print('TEST, The number after modulo stuff is:  '+ str(lowerChosen))
firstNum = letterToNum(lowerChosen)
print('TEST, first number : ' + str(firstNum))
advancedNum = advanceNum(firstNum, advancer)
print('TEST, advanced number is now: ' + str(advancedNum))
encryptedLetter = numberToLetter(advancedNum)
print('The letter ' + str(lowerChosen) + ' advanced by ' + str(advancer) + " becomes: " )
print(str(encryptedLetter))