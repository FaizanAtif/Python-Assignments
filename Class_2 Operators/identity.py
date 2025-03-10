# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)   # True (same object)
print("a is c:", a is c)   # False (different objects)
print("a is not c:", a is not c)  # True
