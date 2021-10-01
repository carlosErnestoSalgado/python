def read():
    numbers = []
    # Abrimos el archivo en modo lectura
    with open("./files/numbers.txt", "r", encoding="UTF-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    # Si no le pasamos como parametro a open() encoding="UTF-8" que es un formato de escritura
    # Rocío lo escribira asi: Roc�o
    names = ['Facundo', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open("./files/names.txt", "w", encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def main():
    # read()
    write()

if __name__=='__main__':
    main()