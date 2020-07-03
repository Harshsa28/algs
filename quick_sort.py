import random

def quick_sort(low, high):
	global lst #make it global so no need to return
	if low < high:  #make sure that it has more than 1 element
		pivot = random.randint(low, high)  #random pivot
		p = partition(low, high, pivot)  #partition around pivot and get the new loc of pivot in p
		quick_sort(low, p-1) #divide n conquer
		quick_sort(p+1, high) #divide n conquer


def partition(low, high, pivot): #partition the list
	global lst   
	i = low             
	fire = lst[pivot]   #value of pivot
	for j in range(low, high+1): 
		if lst[j] < fire:  #if lst[j] < value of pivot, swap
			temp  = lst[i]
			lst[i] = lst[j]
			lst[j] = temp
			i += 1
	index = lst.index(fire) 
	temp = lst[i]  #swap
	lst[i] = lst[index]
	lst[index] = temp
	return i

lst = [2,4,1,4,6,2,5,7,8]
quick_sort(0, len(lst)-1)
print(lst)
