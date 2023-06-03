#Ejercicio de la farmacia
'''
#entradas
precio = int(input('Porfavor ingrese el precio del medicamento: '))

#procesos
descuento = precio * 35 // 100
monto_final = precio -descuento

#salidas
print('El monto final a pagar es: ',monto_final,'$')
print('El descuento es de: ',descuento,'$')
print('El precio actual del producto es: ',precio,'$')'''

#Ejercicio 12

#Entradas
print('Este programa calcula el descuento del 10% y el recargo del 5%')
print('~'*40)
precio_lista= int(input('Ingrese el precio de lista del producto: '))

#Procesos
descuento = precio_lista / 10
precio_contado = precio_lista -descuento
recargo = precio_lista * 5 /100
precio_tarjeta = precio_lista+recargo

#Salidas
print('El precio al contado es: ',precio_contado,'$')
print('El precio con tarjeta es: ',precio_tarjeta,'$')