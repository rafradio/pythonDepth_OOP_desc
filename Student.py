from OpenFile import OpenFile
from Range import Range

class Student:
    firstName = Range()
    lastName = Range()

    def __init__(self, *args):
        self.id = args[0]
        self.firstName = args[1]
        self.lastName = args[2]
        self.gender = args[3]
        self.age = args[4]

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    def __setattr__(self, key, value):
        subjects = ["mathematic", "english", "literature", "hystory"]
        mapping = value if key not in subjects else {'grade': value[0], 'tests': value[1]}
        return object.__setattr__(self, key, mapping)
    
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)
    
    def __repr__(self) -> str:
        subjects = ["mathematic", "english", "literature", "hystory"]
        sum, count = 0, 0
        strStudent = f'Студент {self.fullName} имеет следующую успеваемость:\n'
        for sub in subjects:
            if hasattr(self, sub):
                value = getattr(self, sub)
                strStudent += f'\tПредмет "{sub}": оценка {value["grade"]}; средняя тестов {value["tests"]}\n'
                sum += int(value["grade"])
                count += 1

        strStudent += f'\tСредняя оценка: {sum/count}'
        return strStudent




