""" 
 Crear lista de los 100 primeros numeros naturales al cuadrado
"""

def main():
    # Guardar solo los divisibles por tres de los primeros 100 numeros naturales

    # squares = []
    
    # for num in range(1, 101):
    #     if num%3 == 0:
    #       squares.append(num**2)
        
    # List comprehensions
    # squares = [i**2 for i in range(1, 101) if i % 3 == 0 ] # WOW!!!!!! on one line code :)
    # print(squares)

    # Homework
    my_list  = [i  for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(my_list)

if __name__ == "__main__":
    main()