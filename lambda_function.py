def main():
    # lambda function: es una funcion anonima
    # se escribe en una sola linea de codigo

    # Creare una funcion que identifique si una palabra es un palindrome
    palindrome = lambda string: string == string[::-1]

    print(palindrome('ama'))
if __name__ == '__main__':
    main()