# Write mode ('w') - creates new file or overwrites existing
file = open("notes.txt", "w")
file.write("This is a sample note.\n")
file.write("This is the second line.\n")
file.close()

# Better way - automatically closes file
with open("notes1.txt", "w") as file:
    file.write("This is a sample note using with statement.\n")
    file.write("This is the second line using with statement.\n")
# File automatically closes when indented block ends

# Read entire file
with open("notes1.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("notes1.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes \n at end

with open("notes1.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # List of lines

# Append mode ('a') - adds to end of file

with open("notes.txt", "a") as file:
    file.write("This line is appended.\n")

