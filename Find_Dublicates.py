#!usr/bin/python3
#GITHUB	-> LosGnidoS
#Created by KIRILL SHVEDOV

'''Find out if the array
 has dublicates or not'''

array = [1,2,2,4,4,5,5,6,7,8,9,9,10]
def Find_Dublicates(arr):
	#x = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i != j:
				if (arr[i] == arr[j]):
					#x.append(arr[i])
					return True
	return False
	

