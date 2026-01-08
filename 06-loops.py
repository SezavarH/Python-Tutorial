count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4


# else example
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# break example
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# continue example
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# for loop example
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)  

# prints from 0 to 5
# range example
for i in range(5):  # generates numbers from 0 to 4
    print(i)

# nested loops example
for i in range(3):  # outer loop
    for j in range(2):  # inner loop
        print(f"i: {i}, j: {j}")
