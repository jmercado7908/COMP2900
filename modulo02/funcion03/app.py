def age():
    global currentYear
    global birthYear
    birthYear = 2020
    currentAge = currentYear - birthYear
    print(f'You ager is {currentAge} ')

currentYear = int(input('Current Year: '))
birthYear = int(input('Birth Year: '))

age()
print(birthYear)
