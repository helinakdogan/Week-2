student = {
    "name": "Alex",
    "age": 18,
    "gpa": 3.4
}

print(student)
print(student["name"])
print(student.get("age"))

student["major"] = "Software Engineering" # Adds a new key-value pair
print(student)
student["age"] = 19
print(student)