#lists

# Sample list to work with
vegetables = ["carrot", "broccoli", "spinach"]

# Append
vegetables.append("potato")
print(f"Append: {vegetables}")

# Insert
vegetables.insert(1, "cauliflower")
print(f"Insert: {vegetables}")

# Remove
vegetables.remove("broccoli")
print(f"Remove: {vegetables}")

# Copy
# Shallow Copy
vegetables_shallow_copy = vegetables.copy()
vegetables_shallow_copy[0] = "tomato"  
print(f"Shallow Copy: {vegetables_shallow_copy}, Original: {vegetables}")

# Deep Copy
import copy
vegetables_deep_copy = copy.deepcopy(vegetables)
vegetables_deep_copy[0] = "lettuce"  
print(f"Deep Copy: {vegetables_deep_copy}, Original: {vegetables}")

# Count
vegetables.append("carrot")
carrot_count = vegetables.count("carrot")
print(f"Count of 'carrot': {carrot_count}")

# Extend
more_vegetables = ["cucumber", "pepper"]
vegetables.extend(more_vegetables)
print(f"Extend: {vegetables}")

# Index
carrot_index = vegetables.index("carrot")
print(f"Index of 'carrot': {carrot_index}")

# Sort
vegetables.sort()
print(f"Sort: {vegetables}")

# Reverse
vegetables.reverse()
print(f"Reverse: {vegetables}")

# Clear
vegetables.clear()
print(f"Clear: {vegetables}")

# Pop
removed_vegetable = more_vegetables.pop()
print(f"Pop: {removed_vegetable}, Remaining: {more_vegetables}")

# Sample list to work with
vegetables = ["carrot", "cauliflower", "spinach", "potato", "carrot", "cucumber", "pepper"]

# Slice from index 1 to 4
subset1 = vegetables[1:4]
print("Positive Slicing:", subset1)

# Slice with a step
subset2 = vegetables[1:6:2]
print("Positive Slicing with Step:", subset2)

# Slice the last three elements
subset3 = vegetables[-3:]
print("Negative Slicing:", subset3)

# Slice from the second to last to the fourth to last
subset4 = vegetables[-2:-5:-1]
print("Negative Slicing with Reverse:", subset4)

# Extract a portion of the list
middle_subset = vegetables[2:5]
print("Retrieve a Portion:", middle_subset)

# Update elements within a slice
vegetables[1:3] = ["tomato", "lettuce"]
print("Update a Slice:", vegetables)

# Remove elements within a slice
del vegetables[2:4]
print("Delete a Slice:", vegetables)

# Add elements into a specific position
vegetables[1:1] = ["zucchini", "pumpkin"]
print("Insert into a Slice:", vegetables)


#tuples

# Example with repeated elements
repeated_number = 4  # Number to repeat
repetitions = 2  # Number of repetitions

repeated_tuple = tuple(range(repeated_number)) * repetitions

print("Tuple with repeated elements:", repeated_tuple)
# Output: Tuple with repeated elements: (0, 1, 2, 3, 0, 1, 2, 3)

# Example with a while loop
fruit_tuple = ("mango", "kiwi", "grape")
i = 0
while i < len(fruit_tuple):
    print(fruit_tuple[i])
    i = i + 1


# Example 1: Slicing
veggies_list = ['carrot', 'broccoli', 'cauliflower', 'spinach']
print(veggies_list[:2])  # output: ['carrot', 'broccoli']
print(veggies_list[2:])  # output: ['cauliflower', 'spinach']

# Example 2: Replacing a slice with new elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = [100, 200, 300]
print(numbers)  # output: [1, 2, 100, 200, 300, 6, 7, 8, 9]

# Example 3: Inserting elements into a specific position
numbers[5:5] = [400, 500]
print(numbers)  # output: [1, 2, 100, 200, 300, 400, 500, 6, 7, 8, 9]


#dictionary

sentence = "The cat jumps over the lazy dog."
word_counts = {}

for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

data = [
    {"name": "Ananya", "age": 22, "department": "HR"},
    {"name": "Arjun", "age": 29, "department": "Engineering"},
    {"name": "Priya", "age": 32, "department": "HR"},
    {"name": "Rohan", "age": 36, "department": "Engineering"}
]

# Grouping data by department
grouped_data = {}
for person in data:
    department = person["department"]
    if department in grouped_data:
        grouped_data[department].append(person)
    else:
        grouped_data[department] = [person]

print(grouped_data)
 


