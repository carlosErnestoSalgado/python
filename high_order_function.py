from functools import reduce
def main():

    # Filter Function
    # Filtrar solo los numeros pares
    one_list = [1, 15, 24, 2, 7, 9, 18, 11, 3, 5, 0]
    odd = list(filter(lambda x: x % 2 == 0 , one_list))
    print('List numbers / by 2: ', odd)

    

    # Map Function
    # Elevar al cuadrado una lista
    # La funcion map() recipe como parametros una funcion y un iterable
    # En este caso le pasamos la funcion anonima lambda
    my_list = [1, 2, 3, 4, 5]
    # square = [i**2 for i in my_list] # Metodo con dict_comprehensions
    square = list(map(lambda x:x**2, my_list)) # Metodo con High Order Functions 
    print('Squares list: ',square)

    # Reduce Function
    _list = [2, 2, 2, 2, 2]
    all_multipicated = reduce(lambda a, b: a * b, _list)
    print(f'El resultado de multiplicar todos os valores de la lista {_list} es: {all_multipicated}')

if __name__=='__main__':
    main()