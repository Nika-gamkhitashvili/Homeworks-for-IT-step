import json


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @staticmethod
    def read_json(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    @staticmethod
    def write_json(new_data, json_file):
        with open(json_file, 'w') as file:
            json.dump(new_data, file, indent=4)


students_data = {
    "students": [
        {"name": "Alice", "age": 20, "grades": [85, 90, 75]},
        {"name": "Bob", "age": 21, "grades": [80, 88, 92]},
        {"name": "Charlie", "age": 22, "grades": [70, 75, 65]}
    ]
}


with open('students.json', 'w') as json_file:
    json.dump(students_data, json_file, indent=4)


students_list = []
for student in students_data['students']:
    students_list.append(Student(student['name'], student['age'], student['grades']))


averages = {}
for student in students_list:
    averages[student.name] = round(student.calculate_average(), 2)

students_list[0].write_json(averages, 'averages.json')
