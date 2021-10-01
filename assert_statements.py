def divisor(num):
    assert num > 0, 'Debe ser mayor a 0.'
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = input('Ingresa un numero: ')
    assert num.replace('-','').isnumeric(), 'Debes ingresar un numero'   # .isnumeric() es un metodo para strings que devuelve True si es un numero
    print(divisor(int(num)))
    print('Termino el programa')


if __name__=='__main__':
    main()