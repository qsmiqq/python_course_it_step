s = "some_string"
i = 500
l = [1, 2, 3]
t = (1, 2, 3)

print(dir(s))
print(dir(i))
print(dir(t))
print(dir(l))

print(hash(s))
print(hash(i))

friends = {
    "Ivanov": {
        "id": 1,
        "phone": "+3752964597981",
        "email": 'ivanov@gmail.com'
    }
}

print(friends['Ivanov']['phone'])