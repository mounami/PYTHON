# Loop 5 times
for i in range(5):
    print(f"Count is: {i}")

# Output:
# Loop number 0  ← Python starts counting at 0!
# Loop number 1
# Loop number 2
# Loop number 3
# Loop number 4

#Understanding range():

#range(5) = [0, 1, 2, 3, 4] (5 numbers starting at 0)
#range(1, 6) = [1, 2, 3, 4, 5] (start at 1, stop before 6)
#range(0, 10, 2) = [0, 2, 4, 6, 8] (start, stop, step)

# Print 1 to 10
for i in range(1, 11):
    print(i)

# Count down from 10 to 1
for i in range(10,0,-1):
    print(i)

# Even numbers only
for i in range(0, 21, 2):
    print(i)