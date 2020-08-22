#!usr/bin/python3
#Created by Kirill Shvedov
#GITHUB---->LosGnidoS

import random 

array = [3,1,2,5,6,8,7]
array.sort()
print(array)


def RandomArray(arr):
	max_i = len(arr) - 1
	for i in range(len(arr)):
		j = random.randint(i, max_i)
		arr[i], arr[j] = arr[j], arr[i]
	return arr

print(RandomArray(array))