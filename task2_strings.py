# Task 2: String Processing

sentence = "  Hello, World! Welcome to Python.  "

print("Original:", sentence)
print("Stripped:", sentence.strip())
print("Uppercase:", sentence.strip().upper())
print("Lowercase:", sentence.strip().lower())
print("Replace:", sentence.strip().replace("Python", "Programming"))
print("Split:", sentence.strip().split(" "))
print("Starts with 'Hello':", sentence.strip().startswith("Hello"))
print("Ends with 'Python.':", sentence.strip().endswith("Python."))
print("Character count:", len(sentence.strip()))

first_name = "Donte"
last_name = "Smith"
full_name = f"{first_name} {last_name}"
print("Full Name:", full_name)
print("Reversed:", full_name[::-1])
