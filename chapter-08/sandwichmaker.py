import pyinputplus as pyip

breadPrice = {'wheat':3, 'white':2, 'sourdough':2.5}
proteinPrice = {'chicken':5, 'turkey':8, 'ham':4, 'tofu':3}
cheesePrice = {'cheddar':6, 'Swiss': 8, 'mozarrella':4}
extrasPrice = {'mayo':1, 'mustard':1.5, 'lettuce':1, 'tomato':2}

unitPrice = 0
total = 0

bread = pyip.inputMenu(list(breadPrice.keys()), "\nPlease select your choice of Bread:\n")
unitPrice += breadPrice[bread]

protein = pyip.inputMenu(list(proteinPrice.keys()), "\nPlease select your choice of Protein:\n")
unitPrice += proteinPrice[protein]

if pyip.inputYesNo("\nDo you want cheese? ") == 'yes':
    cheese = pyip.inputMenu(list(cheesePrice.keys()))
    unitPrice += cheesePrice[cheese]

for extra in list(extrasPrice.keys()):
    if pyip.inputYesNo("\nDo you want %s? "%(extra)) == 'yes':
        unitPrice += extrasPrice[extra]

units = pyip.inputInt("\nHow many sandwiches do you want? ")

total = units*unitPrice

print("\nYour total amount is",total)
