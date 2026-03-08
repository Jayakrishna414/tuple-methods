# Tuple example
t = (10, 20, 30, 20, 40, 20, 50)

# count() method – counts occurrences of an element
print("Count of 20:", t.count(20))

# index() method – returns index of first occurrence
print("Index of 30:", t.index(30))

# Additional useful tuple operations
print("Length of tuple:", len(t))
print("Maximum value:", max(t))
print("Minimum value:", min(t))
print("Sum of elements:", sum(t))

# Iterating through tuple
print("Tuple elements:")
for i in t:
    print(i)

# Membership test
print("Is 40 present in tuple?", 40 in t)

# Tuple concatenation
t2 = (60, 70)
print("Concatenated tuple:", t + t2)

# Tuple repetition
print("Repeated tuple:", t * 2)
