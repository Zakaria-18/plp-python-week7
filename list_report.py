# list_report.py
# Numbered list, count of long names, and the longest name - all with loops.

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Print each item numbered: 1. bread, 2. avocado, ...
print("Numbered list:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# 2. Count how many item names have more than 4 letters
long_count = 0
for item in items:
    if len(item) > 4:
        long_count += 1
print("Items with more than 4 letters:", long_count)

# 3. Find the longest item name using a loop comparison (no max() shortcut)
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item:", longest)
