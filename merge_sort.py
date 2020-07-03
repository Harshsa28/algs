import math   #for floor


def merge_sort(lst):
	if len(lst) < 2:    #if len is 1, return the list
		return lst
	mid = math.floor(len(lst)/2)   
	lst1 = merge_sort(lst[0:mid])  #simple divide n conquer
	lst2 = merge_sort(lst[mid:len(lst)]) #simple divide n conquer
	return merge(lst1, lst2)  #merge the 2 smaller sorted lists



def merge(lst1 , lst2):
	len1 = len(lst1)
	len2 = len(lst2)
	lst3 = []
	i = 0
	j = 0
	while (True):
		if lst1[i] <= lst2[j]:
			lst3.append(lst1[i])
			i += 1
		else:
			lst3.append(lst2[j])
			j += 1
		if i == len1 or j == len2:
			break
	
	if i == len1:
		while j != len2:
			lst3.append(lst2[j])
			j += 1
	if j == len2:
		while i != len1:
			lst3.append(lst1[i])
			i += 1
	return lst3


lst = [2,4,1,4,6,2,5,7,8]
#lst = [2,5,7,8]
print(merge_sort(lst))
