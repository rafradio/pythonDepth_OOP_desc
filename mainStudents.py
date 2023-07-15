from Student import Student
from ParseFile import ParseFile

def main():
    students = []
    with ParseFile() as st:
        
        for s in st:
            students.append(s)


    print(students)
    print(dir(students[2]))
    print(students[0].mathematic)

if __name__ == '__main__':
    main()