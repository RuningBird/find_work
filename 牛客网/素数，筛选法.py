N = 20
arr = [i for i in range(2, N + 1)]

for i in arr:
    for j in arr[arr.index(i):]:
        try:
            arr.remove(i+i)
            arr.remove(j+i)
        except:
            pass

print(arr)