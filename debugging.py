def divisor(num):
    # List comprehensions
    divisors = [i for i in range(1, num + 1 )if num % i == 0]
    return divisors

def main():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisor(num))
        print('Termino el programa')
    except ValueError:
        print('Debes ingresar un numero.')

if __name__=='__main__':
    main()