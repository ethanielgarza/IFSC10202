user_input = input("Enter a value separated by spaces: ")
elements = user_input.split(' ')
numbers = []
for i in range(len(elements)):
    numbers.append(int(elements[i]))
if len(numbers) > 0:
    distinct_count = 1
else:
    distinct_count = 0
for i in range(1,len(numbers)):
    if numbers[i] != numbers[i - 1]:
        distinct_count += 1
print("Number of Distinct Elements: ", distinct_count)