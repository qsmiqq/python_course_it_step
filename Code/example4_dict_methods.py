# UPDATE
students = {"name": "Nick", "age": 19, "course": "Python"}
print(students)

students["name"] = "Mike" # update
students["school"] = "Primary school" # add
print(students)

students.update({"rate": 10})
print(students)

# REMOVE

del students["rate"]
print(students)
students.setdefault("ages", 20)
print(students)
students.clear()
print(students)