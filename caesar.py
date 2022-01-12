#shift letters by the number provided, start with constants
chosenLet = 'D'    #input('what letter to start with?')
chosenNum = 2      #int(input('How much to shift by?'))

lowerChosen = chosenLet.lower()
print(lowerChosen)

def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case 'c':
            return 3   # 0 is the default case if x is not found
        case 'd':
            return 4
        case 'e':
            return 5
        case 'f':
            return 6
        case _:
            return 0  # 0 is the default case if x is not found

if chosenNum <=26:
    print('we can do this wihout worrying about remainders')
else:
    #what to do with remainders?
    print('do something with remainders')