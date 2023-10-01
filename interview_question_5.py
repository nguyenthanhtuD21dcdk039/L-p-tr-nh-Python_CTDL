def find_duplicates(arr):
    flags = [False] * len(arr)
    result = []

    for x in arr:
        if flags[x]:
            result.append(x)
        else:
            flags[x] = True

    return result


arr = [1, 2, 2, 1, 5, 6, 7, 8, 5]

print(find_duplicates(arr))
