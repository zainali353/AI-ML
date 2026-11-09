## my first API
import json

# student = {
#     "name": "Zain",
#     "skills": ["Python", "SQL"],
#     "semester": 6
# }

# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)


with open("Student.json", "r") as file:
    student = json.load(file)

print(student["name"])
print(student["skills"])

