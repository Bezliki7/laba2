import random

choices = ['камень', 'ножницы', 'бумага']

def declareGameResult(userChoiceIndex, computerChoiceIndex):
    if userChoiceIndex == computerChoiceIndex:
        print('ничья!')
    elif (userChoiceIndex == 0 and computerChoiceIndex == 1) or \
         (userChoiceIndex == 1 and computerChoiceIndex == 2) or \
         (userChoiceIndex == 2 and computerChoiceIndex == 0):
        print('ты победил 🎉')
    else:
        print('компьютер победил 🤖')

def startGame():
    try:
        print('0 - камень \n1 - ножницы \n2 - бумага')
        userChoiceIndex = int(input("Введите цифру из списка: "))
        computerChoiceIndex = random.randrange(0, 3)

        userChoice = choices[userChoiceIndex]
        computerChoice = choices[computerChoiceIndex]

        print(f'твой выбор: {userChoice}, выбор компьютера: {computerChoice}')

        declareGameResult(userChoiceIndex, computerChoiceIndex)
    except:
        print('неверный ввод')

startGame()

while True:
    userInput = input("Введите c, чтобы продолжить: ")
    if userInput == "c":
        startGame()
    else:
        break
