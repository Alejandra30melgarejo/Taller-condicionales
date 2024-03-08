import math 
# programar para calcular el porcentaje de ganancia de un articulo vendido 

# input 
precio_costo = float(input ("ingrese el valor del producto: "))
ganancia = 0
precio_venta = precio_costo+ganancia

#proccessing

if precio_costo < 3000:
    ganancia = precio_costo *0.15
elif precio_costo > 6000:
    ganancia = precio_costo *0.25
else:
    ganancia =500

precio_venta = (precio_costo + ganancia)
#output
print("el producto tiene un precio final de",precio_venta,)

