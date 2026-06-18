# add(element) - Adds an element to the set. If the element already exists, it does nothing.
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

# remove(element) - Removes an element from the set. If the element doesn't exist, it raises a KeyError.
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

# discard(element) - Removes an element from the set. If the element doesn't exist, it does nothing.
numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

# intersection
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

# difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}
