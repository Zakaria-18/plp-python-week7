# list_warmup.py
# Warm up with list basics: index access, .append(), .remove(), and len().

fruits = ["apple", "banana", "mango", "orange"]

# Print the first and last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Append a fifth fruit and print the whole list
fruits.append("pineapple")
print("After append:", fruits)

# Remove one fruit and print the list again
fruits.remove("banana")
print("After remove:", fruits)

# How many fruits remain?
print("Number of fruits:", len(fruits))
