# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Hello world")
# Set geometry (widthxheight)
root.geometry('350x200')
 
# all widgets will be here
# Execute Tkinter
root.mainloop()


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