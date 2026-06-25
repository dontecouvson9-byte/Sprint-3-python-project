# Task 3: Lists and Tuples

# Lists
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print("Original list:", fruits)
fruits.append("grape")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
fruits.sort()
print("Sorted:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Sliced (1-3):", fruits[1:3])
print("Length:", len(fruits))

# Tuples
coordinates = (29.7604, -95.3698)
print("\nTuple (coordinates):", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])
print("Tuple length:", len(coordinates))

# Tuple unpacking
lat, lon = coordinates
print(f"Unpacked — Lat: {lat}, Lon: {lon}")
