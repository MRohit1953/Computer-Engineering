
num_arrays = int(input("Enter the number of arrays: "))
arrays = []

for i in range(num_arrays):
    array = list(map(int, input("Enter the values of array {} separated by space: ".format(i + 1)).strip().split()))
    arrays.append(array)





