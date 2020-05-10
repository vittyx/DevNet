'''
Created on 01 may. 2020
@author: bugosovi
Calculadora Basica Py
'''
import math


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def exponencial(num1, num2):
    if num2 == 0:
        return 1
    return num1 ** num2

def raizCuadrada (num1):
    if num1 == 0:
        return 0
    return math.sqrt(num1)

def mostrarMenu():
    print("*******************************************************")
    print("\n CALCULADORA ", end="\n\t")
    print("0-SUMA.",
          "1-RESTA.",
          "2-MULTIPLICACION",
          "3-DIVISION",
          "4-EXPONENCIAL",
          "5-RAIZ CUADRADA",
           sep="\n\t", end="\n")
    
    print("9-SALIR\n")
    print("*******************************************************")
    
    
# MAIN #
mostrarMenu()

while(True):
    try:
        operador= int(input("\n escoge operador: "))
        if (operador==9):
            break
        else:
            if(operador >=0) and (operador <6):
                if (operador==5):
                    num1 = float(input("\n primer numero: "))
                    print("la raiz cuadrada de:"+str(num1) +"es :"+str(raizCuadrada(num1)))
                else:
                    num1 = float(input("\n primer numero: "))
                    num2 = float(input("\n segundo numero: "))
                    if(operador==0):
                        print("\n la suma de:"+str(num1) +"+"+str(num2) +" = "+ str(suma(num1, num2)))
                    elif(operador==1):
                        print("\n la resta de:"+str(num1) +"+"+str(num2) +" = "+str(resta(num1, num2)))
                    elif(operador==2):
                        print("\n la multiplicacion de:"+str(num1) +"+"+str(num2) +" = "+ str(multiplicacion(num1, num2)))
                    elif(operador==3):
                        print("\nla division de:"+str(num1) +"+"+str(num2) +" = "+ str(division(num1, num2)))
                    else:
                        print("\n"+str(num1) +"elevado a "+str(num2) +" = "+ str(exponencial(num1, num2)))
            else:
                print ("\nPor favor seleccione una opcion del Menu.")
             
    except ZeroDivisionError:
        print("Error al dividir por 0")
        mostrarMenu()
    




print("*******************************************************")
print("Muchas gracias por haber utilizado la calculadora\n")
print("*******************************************************")