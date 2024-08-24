import random

def passwordGenerator():
    lowerchars = ('a','b','c','d','e')
    upperchars = ('A','B','C','D','E')
    specialchars = ('!','*','&')
    numericchars = ('1','2','3','4','5')  # Change integers to strings
    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)
    password = password + password  # If you want to double the password, otherwise this line can be removed.
    return password

print(passwordGenerator())

    
