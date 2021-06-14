'''
question: reverse the item at first index to the item at last index and item at last index to the item at first index.
'''


def main(myList):
    x = myList[0]
    y = myList[-1]
    myList.pop(0)
    myList.pop(-1)
    myList.append(x)
    myList.insert(0, y)
    print(myList)

myList = [10, 20, 50, 80]
main(myList)
