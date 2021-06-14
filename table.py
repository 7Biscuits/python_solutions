'''
question: Make a function called "table" which will return a list of the calculated values of the given number to the given limit.
'''

# soulution:

def table(num_1, num_2):
    myList = []
    for x in range(1, num_2 + 1):
        element = num_1 * x
        myList.append(element)
        print(myList)
table(2, 10)
