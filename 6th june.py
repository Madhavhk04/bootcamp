print("hello world")
a=10
b=20
c=a+b
print=c

a = 10
b = 5

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

    # Jumping Statements
# break statement
for i in range(15):
    if i == 8:
        break
    print(i)

# continue statement
for i in range(15):
    if i == 8:
        continue
    print(i)

def welcome(user): # Function definition with parameter 'user'
    
    print("Welcome", user + "!")

# Function with argument 'aadhil'
welcome("aadhil")

#posistional arguments

def compute_area(height, breadth):
    return height * breadth


area = compute_area(7, 4)  
print(area)  

#OOPS

difference = lambda m, n: m - n

result = difference(15, 6)
print(result)  # Output: 9

