""" numeros = [13,23,45,6,67,123]

def numero_par (numero):
    return numero*3

#Definir la función
numero_par = list(map(numero_par, numeros))
print(numero_par)

lista=[45,50,91,80,54]

def multiplo_de_5(numeros):
    if numeros % 5 ==0:

        return print("es normal")
    else:
        return print("sigue")

multiplo_de_5 = list(filter(multiplo_de_5, lista))
precios=[34,50,45,100,450,230]

def precios_con_iva(numero):
    return round(numero * 1.16,2)

precios_con_iva= list(map(precios_con_iva, precios))

def precios_con_descuento(numero):
    if numero > 50 and numero < 100:
        return numero
    else: 
         0

precios_con_descuento = list(filter(precios_con_descuento, precios_con_iva))
porcentaje_precios_descuento= round((len(precios_con_descuento)/len(precios_con_iva)*100),2)

print(precios_con_descuento)
print(f'porcentaje_precios_descuento {porcentaje_precios_descuento} %') """

#El dueño de la tienda en linea pozole mio, necesita saber 
# cuantos de sus productos son acredores a paquetes de envió de $90 o $150.
#Los productos con precio con IVA que rebasen los $150 deberán ocupar el paquete de envió de $90.
# Por lo contrario usaran el paquete de $150.
precios_sin_iva = [3, 148, 74, 71, 4, 83, 95, 20, 61, 10, 69, 67, 23, 164, 97, 67, 144, 200, 38, 90, 200, 162, 6, 180, 65, 71, 90, 182, 16, 132, 182, 108, 90, 196, 48, 2, 158, 88, 39, 39, 54, 80, 89, 3, 90, 170, 88, 71, 142, 45, 81, 194, 36, 39, 30, 33, 38, 44, 134, 43, 12, 52, 170, 162, 192, 83, 18, 176, 120, 28, 86, 188, 51, 11, 96, 13, 198, 34, 66, 23, 200, 62, 194, 91, 51, 26, 152, 186, 86, 38, 46, 66, 83, 66, 40, 2, 20, 12, 91, 53]

def precios_con_iva(numeros):
    return round(numeros*1.16,2)
precios_con_iva = list(map(precios_con_iva, precios_sin_iva))

#paquetes de envio catalogados con $90
def paquete_1_90(numeros):
 if numeros> 150:
     return True
paquete_1_90 = list(filter(paquete_1_90, precios_con_iva))

def paquete_2_150(numeros):
    if numeros < 150:
        return True
paquete_2_150 = list(filter(paquete_2_150, precios_con_iva))


paq_90 = round( len(paquete_1_90)/len(precios_con_iva),2)* 100
paq_150 = round(len(paquete_2_150)/len(precios_con_iva),2)*100

print(f'porcentaje con paquete de envío $90:{paq_90} %')
print(f'Porcentaje con paquete de envío $150: {paq_150}%')