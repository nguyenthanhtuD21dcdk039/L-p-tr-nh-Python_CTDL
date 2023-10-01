print("Hello from Pycharm and Python!")
array = [20, 32, 14, 28, 10, 2003]

max = array[0]
min = array[0]
for num in array:
    if num > max:
        max = num
    if num < min:
        min = num
print(min)
print(max)
