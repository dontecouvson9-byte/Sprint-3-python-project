# Task 5: Dictionaries

person = {
    "name": "Donte",
    "city": "Midland",
    "state": "Texas",
    "skills": ["Python", "SQL", "Google Sheets"],
    "enrolled": True
}

print("Full dictionary:", person)
print("Name:", person["name"])
print("City:", person.get("city"))
print("Skills:", person["skills"])

# Add and update
person["bootcamp"] = "TripleTen"
person["city"] = "Midland, TX"
print("\nAfter update:", person)

# Delete a key
del person["enrolled"]
print("After delete:", person)

# Loop through dictionary
print("\nAll key-value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Dictionary methods
print("\nKeys:", list(person.keys()))
print("Values:", list(person.values()))
