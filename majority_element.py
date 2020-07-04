import math

def majority_element(lst):
	number = {}
	majority = math.floor(len(lst)/2)
	for i in range(len(lst)):
		if lst[i] in number:
			number[lst[i]] += 1
		else:
			number[lst[i]] = 1
		if number[lst[i]] > majority:
			print("list is :", lst)
			print("majority element is :", lst[i] )
			return
	print("list is :", lst)
	print("no majority element")
	return

majority_element([1,3,1,6,7,1,1])
majority_element([1,2,3,4,5,6])

