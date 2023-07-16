from OpenFile import OpenFile
from Student import Student
import asyncio

class ParseFile:
    def __enter__(self):
        with OpenFile('students.csv') as of:
            for row in of:
                st = Student(*row)
                yield asyncio.run(self.checkGrades(st))

    
    def __exit__(self, *args, **kwargs):
        pass
    
    async def checkGrades(self, obj):
        with OpenFile('grades.csv') as of:
            for row in of:
                if int(obj.id) == int(row[0]):
                    testAverage = await self.testsCheck(obj.id, row[1]) 
                    setattr(obj, row[1], (row[2], testAverage))
        return obj
    
    async def testsCheck(self, id, subject):
        sum, count = 0, 0
        with OpenFile('tests.csv') as of:
            for row in of:
                if int(row[1]) == int(id) and row[0] == subject:
                    sum += int(row[2])
                    count += 1

        return sum / count if count != 0 else None
            
        