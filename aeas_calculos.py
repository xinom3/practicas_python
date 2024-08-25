opcion = int(input("Hola amigos bienvenidos a mi programa\nvamos a calcular el area de algunas figuras elige alguna de las siguientes\nCuadrado : 1\nRectangulo : 2\nCirculo : 3\nOpciopn : "))

if opcion == 1:
    cuadrado_lado = float(input("Introduce el lado del cuadrado : "))
    area_cuadrado = round(pow(cuadrado_lado,2),2)
    print(f"El area del cuadrado es {area_cuadrado} M2")

# If opcion == 2:
    
