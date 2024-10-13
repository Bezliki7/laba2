def getOddNumbers(end):
    for number in range(end):
        if (number % 2):
            yield number

oddNumbers = list(getOddNumbers(30))

for i in range(len(oddNumbers)):
    if (not i or i == 4 or i == len(oddNumbers) -1):
        print(f'oddNumbers[{i}] = {oddNumbers[i]}')
    
