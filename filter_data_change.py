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
    # Usung High Order Function
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'] , all_python_devs))
    all_teacher = list(filter(lambda worker: worker['position'] == 'Teacher', DATA))
    all_teacher = list(map(lambda worker: worker['name'], all_teacher))
    # Using List Comprehesions
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    young_people = [worker | {'young': True} for worker in DATA if worker['age'] < 23]
    # Show for console
    for worker in young_people:
        print(worker)

if __name__=='__main__':
    main()