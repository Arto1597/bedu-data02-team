numeros = ['3', '148', '74', '71', '4', '83', '95', '20', '61', '10', '69', '67', '23', '164', '97', '67', '144', '200', '38', '90', '200', '162', '6', '180', '65', '71', '90', '182', '16', '132', '182', '108', '90', '196', '48', '2', '158', '88', '39', '39', '54', '80', '89', '3', '90', '170', '88', '71', '142', '45', '81', '194', '36', '39', '30', '33', '38', '44', '134', '43', '12', '52', '170', '162', '192', '83', '18', '176', '120', '28', '86', '188', '51', '11', '96', '13', '198', '34', '66', '23', '200', '62', '194', '91', '51', '26', '152', '186', '86', '38', '46', '66', '83', '66', '40', '2', '20', '12', '91', '53']
def multiplicar_por_9(numero):
    return numero * 9
def convertir_a_enteros(numero):
    return int(numero)
def convertir_true_pares(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
# Convertir strings a numeros
numeros_enteros = list(map(convertir_a_enteros, numeros))
# Multiplicar cada numero por 9
numeros_por_9 = list(map(multiplicar_por_9, numeros_enteros))
# Convertir pares a True
numeros_pares_true = list(map(convertir_true_pares, numeros_por_9))
print(numeros_pares_true)