import datetime
import re
import math

date = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d\d$'

userInput = input("Введите дату рождения в формате день/месяц/год: ")

if (re.match(date, userInput)):
    splitted = userInput.split('/')
    d, m, y = splitted[0], splitted[1], splitted[2]

    today = datetime.date.today()
    birhday = datetime.date(int(y), int(m), int(d))

    diff = today - birhday
    yo = diff.days / 365
    print(f'Вам сейчас: {math.floor(yo)} :)')
else:
    print("Неверный фломат")
