
#OOPS

difference = lambda m, n: m - n

result = difference(15, 6)
print(result)  # Output: 9

class Counter:
    
    def add_one(self):
        if not hasattr(self, 'count'):
            self.count = 0  # Initialize the count variable if it doesn't exist
        self.count += 1  # Increment the count variable
        return self.count  # Return the updated value of the count variable

counter = Counter()  # Creating an instance of the Counter class

print(counter.add_one())  # Output: 1  # Printing the initial value of the count variable after incrementing
print(counter.add_one())  # Output: 2  # Printing the updated value of the count variable after incrementing
