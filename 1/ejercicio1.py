#programa para calcular en que cuadrante estan un punto, de un plano cartesiano

#entrada
x = int(input("ingrese la coordenada x: "))
y =int(input("ingrese la coordenada y: "))

#proceso y salida 
if x == 0:
    if y == 0:
        print("la coordenada" ,(x , y),"esta en el origen")
    else:
        print("la coordenada",(x , y),"esta en el eje y")
elif y == 0:
    print("la coordenada" ,(x , y),"esta en el eje x")
elif x > 0:
    if y > 0:
        print("la coordenada" ,(x , y),"esta en el cuadrante 1")
    else:
        print("la coordenada" ,(x , y),"esta en el cuadrante 4")
elif y < 0:
    print("la coordenada" ,(x , y),"esta en el cuadrante 3")
else:
    print("la coordenada" ,(x , y),"esta en el cuadrante 2")
        
