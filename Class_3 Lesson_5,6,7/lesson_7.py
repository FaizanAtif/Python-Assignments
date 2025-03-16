# Lesson 07: Sets & Frozensets

# Set Example (Mutable, Unordered)
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(3)
print("Set after modifications:", numbers)


# Frozenset Example (Immutable Set)
immutable_numbers = frozenset([10, 20, 30, 40])
print("Frozenset:", immutable_numbers)


# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)  # Union
print("Intersection:", set1 & set2)  # Intersection
print("Difference:", set1 - set2)  # Difference
