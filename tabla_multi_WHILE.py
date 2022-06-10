# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:57:54 2022

@author: Patricio Haro
"""
ninicio=int(input("Ingrese desde que tabla desea operar: ")) # variable ninicio.
nfinal=int(input("Ingrese hasta que tabla desea operar: ")) # variable nfinal.


while (ninicio > nfinal): # condicion numero ninicio debe ser menor que nfinal.
     print("Error digita el numero inicial, menor que el final.") # imprime error de la condicion.
     ninicio=int(input("Ingrese desde que tabla desea operar: ")) # variable ninicio.
     nfinal=int(input("Ingrese hasta que tabla desea operar: ")) # variable nfinal.


variable=int(input("cuantos filas desea operar por tabla: ")) # variable de filas a impirmir.

while variable<1: # condicion para bloqueo de variable debe ser mayor que 1.
     print("numero de fila incorrecto, el valor ingresado debe ser mayor que 0 ")
     variable=int(input("cuantos filas desea operar por tabla: "))


while ninicio<nfinal+1: # se da rango al valor con ninicio y nfinal+1.
    suma=0 # barrido de suma.
    promedio=0 # barrido de promedio.
    print("La Tabla de N°:",ninicio) # se manda imprimir la variable j para verificacion de tablas.
    print("\n") # salto de linea
    par=0
    impar=0
    i=1
    while i<variable+1: # rango en de la variable de 1 a variable+1.
        res=i*ninicio # calculo de resultado producido de i*inicio.
        suma+=res # calculo de suma.
        promedio=suma /variable # calculo del promedio de las sumas 
        print(i,"x",ninicio,"=",res) # imprimir ixinicio y respuesta.
        if res%2==0: # condicional de pares e impares. 
            par=par+1 # si la condicion se cumple adopta esta indicacion de lo contrario impar.
        else:
            impar=impar+1 # se cumple la condicion si en la condion par no se cumplio.
        i=i+1 # condicion para regresar a while i<variable+1.
    ninicio=ninicio+1 # condicion para regresar a while ninicio<nfinal+1.
    
    
    
    print("La 'SUMA' de los números es:",suma) # imprime la suma de los numeros resultantes. 
    print("El 'PROMEDIO' de los números es:",promedio) # imprime el promedio del resultado.
    print("Hay",par,"números pares.") # muestra el numero de pares en los
    # resultados de la multiplicacion efectuada. 
    print("Hay",impar,"números impares.") # muestra el numero de impres en los
    # resultados de la multiplicacion efectuada.
    print("\n"*2) #salto de linea.
    
 
 