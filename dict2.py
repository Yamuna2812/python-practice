students = {"Alice": 85, "Bob": 72, "Charlie": 90}

grades = {}
for name, marks in students.items():
    if marks >= 90:
        grades[name] = "A"
    elif marks >= 75:
        grades[name] = "B"
    else:
        grades[name] = "C"

print(grades)