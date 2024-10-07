def getItems(func):
    items = ['pie', 'chips']

    for item in items:
        yield func(item)

items = getItems(lambda arg: f'take {arg} and eat it')

for item in items:
    print(item)