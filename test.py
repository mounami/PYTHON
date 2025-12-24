def calculate(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

data = [5, 10, 15]
result = calculate(data)
new_result = calculate([result, 20])
print(new_result)