def mcd(a,b):
    if(b==0):
        return a
    else:
        return mcd(b,a%b)

def cadena_repetida(palabra,veces):
    if veces == 0:
        return ""
    else:
        return palabra+cadena_repetida(palabra,veces-1)

def cuenta_letras(cadena,letra):
    if not cadena:
        return 0
    return (1 if cadena[0] == letra else 0) + cuenta_letras(cadena[1:], letra)

def binario_decimal(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binario_decimal(n // 2) + str(n % 2)

def calcula_digitos(n):
        n = abs(n)
        if n < 10:
            return 1
        return 1 + calcula_digitos(n // 10)

def menu():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1. Calcular MCD")
        print("2. Repetir palabra")
        print("3. Cuenta cuantas veces aparece una letra")
        print("4. Conversion de decimal a binario")
        print("5. Calcula cuantos digitos tiene un numero")
        print("6. Salir")

        opcion=input("Elija una Opcion: ")

        match opcion:
            case "1":
                a=int(input("Ingrese el primer numero: "))
                b=int(input("Ingrese el segundo numero: "))
                print("el MCD de",a,"y",b,"es: ",mcd(a, b))
            case"2":
                palabra=input("Ingrese la palabra: ")
                veces= int(input("Cuantas veces quiere repetirlo: "))
                print("Resultado: ",cadena_repetida(palabra,veces).__str__())
            case"3":
                cadena = input("Ingresa la cadena: ")
                letra = input("Ingresa la letra a buscar: ")
                print(f"La letra '{letra}' aparece {cuenta_letras(cadena, letra)} veces.")
            case "4":
                numero = int(input("Ingresa un número decimal: "))
                print("Binario:", binario_decimal(numero))
            case"5":
                numero=int(input("Ingrese un numero: "))
                print("Resultado: ","el numero tiene",calcula_digitos(numero),"digitos")

menu()



