from faker import Faker
import json

fake = Faker()


class Student:
    def __init__(self, name, age, active):
        self.name = name
        self.age = age
        self.active = active

    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'active': self.active
        }


students = []
for _ in range(100):
    students.append(Student(fake.name(), fake.random_int(min=18, max=25), fake.boolean()))


students_json = json.dumps([student.serialize() for student in students], indent=2)


with open('students.json', 'w') as file:
    file.write(students_json)
