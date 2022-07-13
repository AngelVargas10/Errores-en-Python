DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # all_pythons_devs = [worker["name"]for worker in DATA if worker ["language"]=="python"]
    all_pythons_devs = list(filter(lambda i:i["language"]=="python",DATA))
    all_pythons_devs= list(map(lambda i:i["name"],all_pythons_devs))

    # all_workers_platzi = [i["name"]for i in DATA if i ["organization"]=="Platzi" ]
    all_workers_platzi =list(filter(lambda i:i["organization"]=="Platzi",DATA))
    all_workers_platzi = list(map(lambda i:i["name"],all_workers_platzi))

    adults = [i["name"] for i in DATA if i["age"] > 18]
    # adults = list(filter(lambda i :i["age"] > 18 ,DATA))
    # adults = list(map(lambda i:i["name"],adults))


    # old_people = list(map(lambda i:i and {"old": i["age"] > 70},DATA ))
    #esta la manera mas sencilla 
    # old_people =[i["name"] for i in DATA if i["age"] > 70]
    #manera unpoco mas compleja 
    old_people =list(filter(lambda i:i["age"] > 70,DATA))
    old_people = list(map(lambda i:i["name"],old_people))

    # for i in old_people:
    #     print(i)
    
    for i in old_people:
        print(i)

    for i in adults:
        print(i)
    
    for i in all_workers_platzi:
        print(i)

    for worker in all_pythons_devs:
        print(worker)



if __name__ == "__main__":
    run()