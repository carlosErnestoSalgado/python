DATA = [
    {
        'name': 'Carlos',
        'age': 21,
        'organization': 'Python Corporation',
        'position': 'Language Maker',
        'language': 'python'
    },
    {
        'name': 'Facundo',
        'age': 26,
        'organization' : 'Platzi Online College',
        'position': 'HeadTeacher',
        'language': 'C#'
    },
    {
        'name': 'Laura',
        'age': 23,
        'organization' : 'C College',
        'position': 'Teacher',
        'language': 'C++ '
    },
    {  
        'name': 'Lorenzo',
        'age': 23,
        'organization' : 'C College',
        'position': 'Teacher',
        'language': 'C++ '
    },
    {
        'name': 'Patricia',
        'age': 24,
        'organization': 'Python Corporation',
        'position': 'Language Maker',
        'language': 'python'
    },
    {
        'name': 'Eddy',
        'age': 21,
        'organization': 'Python Corporation',
        'position': 'Language Maker',
        'language': 'python'
    },
    {
        'name': 'Elizabeth',
        'age': 23,
        'organization' : 'C College',
        'position': 'Teacher',
        'language': 'C++ '
    },
    {
        'name': 'Reinaldo',
        'age': 26,
        'organization' : 'Platzi Online College',
        'position': 'HeadTeacher',
        'language': 'C#'
    }
]

def main():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]== 'python'] # Extraemos los que trabajan en python
    all_teacher = [worker['name'] for worker in DATA if worker['position'] == 'Teacher'] # Extraemos los que trabajan como profesores
    adults = list(filter(lambda worker: worker['age'] > 18 , DATA)) # Extraemos los mayores a 18 
    adults = list(map(lambda worker: worker['name'], adults)) # mapeamos la lista adults para tener solo sus nombres
    young_people = list(map(lambda worker: worker | {'young': worker['age'] < 23}, DATA)) # Sumamos al diccionario el par yong:<bool> si es menor a 23 anos
    # En esta ultima linea de codigo es nuevo el metodo de sumar diccionarios q es mediante |
    # Ejemplo {'1': 1} | {'2': 2} = {'1': 1, '2', 2}
 
    for worker in young_people:
        print(worker)
    

if __name__=='__main__':
    main()