def multiplicar(numero):
    return numero *2










numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
new_numbers =[]

#primera opción
"""for n in numbers:
    print(n*2)"""

for n in numbers:
    print(multiplicar(n))

for n in numbers: 
    new_numbers.append(multiplicar(n))

    print(new_numbers)