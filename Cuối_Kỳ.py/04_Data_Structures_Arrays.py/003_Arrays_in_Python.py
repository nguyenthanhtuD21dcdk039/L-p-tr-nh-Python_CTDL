"""
print("Hello world Python!")
print("Ngày Sinh Của Thanh Tú")
array = [2, 8, 28, 10, "Thanh Tú", 2003]
array[0] = "Ngày"
array[1] = "Sinh"
print(array[:])
"""
"""
array = [2, 8, 28, 10, 2003]

max = array[0]

for num in array:
    if num > max:
        max = num

print(max)
"""

array = [2, 8, 28, 10, 2003]

min = array[0]

for num in array:
    if num < min:
        min = num

print(min)
