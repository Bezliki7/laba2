import random

randomNumbersLen = random.randint(10, 15)
randomNumbers = [random.randint(1, 200) for _ in range(randomNumbersLen)]

print((f"Исходные данные: {randomNumbers}"))

try:
    userInput = int(input("Введите цифру X: "))
    
    if (10 > userInput and userInput):
        ans  = filter(lambda randomNumber: randomNumber % userInput == 0 ,randomNumbers)
        print(list(ans))
    else:
        print('Неверный ввод')
except:
    print('Неверный ввод')
