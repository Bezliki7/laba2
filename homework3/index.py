import datetime
import re
import math

datePattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d\d$'
daysInYear = 365

def getDiffYears(y, m, d):
        today = datetime.date.today()
        birhday = datetime.date(y, m, d)

        diff = today - birhday
        res = diff.days / daysInYear
        return res

userInput = input("Введите дату рождения в формате день/месяц/год: ")

if (re.match(datePattern, userInput)):
    splitted = userInput.split('/')
    d, m, y = splitted[0], splitted[1], splitted[2]
    
    yo = getDiffYears(int(y), int(m), int(d))
    if (yo < 0):
        print("Кажется вы еще не родились")
    else:
        print(f'Вам сейчас: {math.floor(yo)} :)')
else:
    print("Неверный фломат")


