def getItems(func):
    items = ['pie', 'chips']

    newItems = []

    for item in items:
        newItems.append(func(item))

    return newItems


items = getItems(lambda arg: f'take {arg} and eat it')
print(items)