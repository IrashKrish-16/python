d = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    d.append(int(input(f"Enter element {i+1}: ")))  # Use formatted string for clear input prompt
print(d)