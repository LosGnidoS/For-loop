#!usr/bin/python3
#GITHUB -> LosGnidoS

'''

Implement searching the largest
 number through function 
 in function.
 /// 1.find_largest(arr) finds the 
 largest number in the array
 /// 2.array_random(new_arr) creates
 the random list of numbers(10)

'''


import random

new_arr = []
def find_largest(arr):
	largest = arr[0]
	for i in range(len(arr)):
		if arr[i] > largest:
			largest = arr[i]
	return largest ," is the largest."



def array_random(new_arr):
	for i in range(10):
		i = random.randint(1,100)
		new_arr.append(i)
	print(new_arr)
	return new_arr

print(find_largest(array_random(new_arr)))
