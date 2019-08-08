array = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
aux = array[0]

for num in array:
    for num2 in array: 
        if aux > array[num]:
            array[num] = aux
            aux = array[num]

print(array)
