def getNewItem(item):
    def closure():
        return f"new {item}" 
    return closure

print(getNewItem("item")())