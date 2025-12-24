print("Hello")
print("Hello")
print("Hello")
# ...97 more times..

for i in range(100):
    print("Hello")

#The WHILE Loop - "Do this until I say stop"

# WHILE loop = repeat as long as condition is True

count = 0

while count <=5:
    print(f"Count is: {count}")
    count +=1  # same as count = count +1
    # CRITICAL: must change count or loop runs forever!
    # Forgot to add: count += 1
    # count stays 1 forever, so loop never stops!

