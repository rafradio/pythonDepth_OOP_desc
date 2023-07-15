from OpenFile import OpenFile

class Student:
    def __init__(self, *args):
        self.id = args[0]
        self.firstName = args[1]
        self.lastName = args[2]
        self.gender = args[3]
        self.age = args[4]

    def __setattr__(self, key, value):
        subjects = ["mathematic", "english", "literature", "hystory"]
        mapping = value if key not in subjects else {'grade': value[0], 'tests': value[1]}
        return object.__setattr__(self, key, mapping)
    
    def __repr__(self) -> str:
        return f'Объект {self.__class__.__name__} {self.firstName} {self.id}'

