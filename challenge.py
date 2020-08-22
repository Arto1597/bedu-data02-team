""" 
import random




number= input("give a number: ")
index = random.randint(1, int(number))
counter = 1 
list_random = []
while counter <= index:
    choice = random.randint(1,2)
    if choice == 1:
        value= str(counter)
    else: 
        value = int(counter)
list_random.append(value)
counter = counter + 1 
print(list_random) """

import random
number = input('Give me a number: ')
index = random.randint(1, int(number))
counter = 1
list_random = []
while counter <= index:
    choice = random.randint(1, 2)
    if choice == 1:
        value = str(counter)
    else:
        value = int(counter)
    list_random.append(value)
    counter = counter + 1
print(list_random)



import random
number = int(input("Cuál es el tamaño de la lista? "))
counter = 1
list_random = []
while counter<=number:
    choice = random.randint(1, 2)
    index = random.randint(1, int(number))
    if choice == 1:
        value = int(counter * index)
    else:
        value = str(counter * index)
    list_random.append(value)
    counter = counter + 1
print(list_random)


