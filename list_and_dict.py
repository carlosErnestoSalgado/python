""" 
    Listas y diccionarios anidados
    Una lista puede contener diccionarios
    Al igual que un diccionario puede contener listas
"""


def main():
    my_list =  [1, "Hello", True, 4.5]
    my_dict = {"first_name":"Carlos", "last_name":"Salgado"}

    super_list= [
        {"first_name":"Carlos", "last_name":"Salgado"},
        {"first_name":"Pedro", "last_name":"Torres"},
        {"first_name":"Leo", "last_name":"Messi"},
        {"first_name":"Cristiano", "last_name":"Ronaldo"}
    ]
    

    super_dict = {
        "naturals_num": [1, 2, 3, 4, 5],
        "intiger_num": [1, -2, 0],
        "floating_num": [4.5, 1.3, 5.7]
    }

    print('Make print to super_dict')
    for key, value in super_dict.items():
       print(key, '-', value)

    print('Make print to super_list')
    for dict in super_list:
        for key, value in dict.items():
            print(key, '-', value)

if __name__ == "__main__":
    main()