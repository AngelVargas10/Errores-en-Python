def divisors(num):
    if num > 0 :
        divisors = [i for i in range(1,num +1) if num % i ==0]
        print(divisors)
        print("Se termino siguiente linea ")
    else:
        print("No sepermiten numeros negativos ")

def run():
    try :
        print("HOLA BIENVENIDO")
        num = int(input("elige un numero :"))
        divisors(num)
    
    except ValueError:
        print("Solo se aceptan numeros")

if __name__ == "__main__":
    run()
