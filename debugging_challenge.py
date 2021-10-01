def divisor(num):
    try:
        if num < 0:
            raise ValueError('No se aceptan numeros negativos.')
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as error:
        print(error)

def main():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisor(num))
        print('Termino el programa')
    except ValueError:
        print('Debes ingresar un numero.')

if __name__=='__main__':
    main()