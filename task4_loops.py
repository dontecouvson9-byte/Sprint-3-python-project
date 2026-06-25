# Task 4: Loops and Conditionals

# For loop
print("For loop — numbers 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# While loop
print("\nWhile loop — countdown:")
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1
print("Liftoff!")

# Loop with list
print("\nLooping through a list:")
tools = ["Python", "SQL", "Google Sheets", "Tableau"]
for tool in tools:
    if tool == "Python":
        print(f"{tool} <-- favorite!")
    else:
        print(tool)

# Nested conditional
print("\nGrade classifier:")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
