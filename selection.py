import random

def selection(lo, nth, hi): #hi is inc
	global lst
	if hi == lo:
		return lst[lo]
	pivot = random.randint(lo, hi)
	p = partition(lo, hi, pivot)
	if nth == p:
		return lst[nth]
	elif nth < p:
		return selection(lo, nth, p-1)
	else:
		return selection(p+1, nth, hi)



def partition(lo, hi, pivot): #hi is inclusive
	global lst
	temp = lst[hi]
	lst[hi] = lst[pivot]
	lst[pivot] = temp
	# pivot is at end
	imp = 0
	for i in range(0, hi):
		if lst[i] < lst[hi]:
			temp = lst[imp]
			lst[imp] = lst[i]
			lst[i] = temp
			imp += 1
	temp = lst[hi]
	lst[hi] = lst[imp]
	lst[imp] = temp
	return imp
				
lst = [2,6,4,1,0]
print(selection(0, 1, len(lst)-1))
