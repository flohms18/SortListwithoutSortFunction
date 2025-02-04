import random

def SortList():
    MyArray = []
    for i in range(10):
        i += 1
        MyArray.append(random.randint(1, 100))
    print("Unsorted List: ", MyArray) 
    
    for i in range(len(MyArray)):
        for j in range(i+1, len(MyArray)):
            if MyArray[i] > MyArray[j]:
                MyArray[i], MyArray[j] = MyArray[j], MyArray[i]
    print("Sorted List: ", MyArray)


SortList()
    