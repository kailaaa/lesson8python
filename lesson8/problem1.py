print('Morbid predictions Program: ')
print('Description: This program asks you for your current age and tells you the year you will die (on average).')
age = input('What is your age today? ')
age = int(age)
birthyear = 2018 - age
birthyear = int(birthyear)
deathyear = birthyear + 79
deathyear = str(deathyear)
print('...thinking...')
print('...thinking...')
print('...thinking...')
print('You will die in the year...' + deathyear)