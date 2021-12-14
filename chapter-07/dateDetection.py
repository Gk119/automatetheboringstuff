import re, sys

dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

text = input("Enter the string: ")

dates = dateRegex.findall(text)

if len(dates) == 0:
    print('No dates found')
    sys.exit()

for date in dates:
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if month not in range(1,13):
        print('Invalid Date')
        continue

    if month in [1,3,5,7,8,10,12]:
        if day > 31 :
            print('Invalid Date')
            continue

    elif month in [4,6,9,11]:
        if day > 30 :
            print('Invalid Date')
            continue
       
    elif year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0):
        if month == 2:
            if day > 29:
                print('Invalid Date')
                continue
    else:
        if month == 2:
            if day > 28:
                print('Invalid Date')
                continue

    print('date:\n', 'day: ', day, ' month: ', month, ' year: ', year, sep = '', end = '\n\n')