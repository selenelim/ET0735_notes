score = 75

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
else:
    grade = 'F'

print("Grade:", grade)



marks = [75, 80, 90, 60]

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", round(average, 2))


student = {
    "name": "Alice",
    "age": 20,
    "scores": [85, 90, 78]
}

# Access values
print("Name:", student["name"])
print("Math score:", student["scores"][0])  # First subject

