from statistics import median

def median_2_sorted(lst1, lst2):
	len_lst1 = len(lst1)
	len_lst2 = len(lst2)
	if len_lst1 == 0:
		return median(lst2)
	if len_lst2 == 0:
		return median(lst1)
	median_index = (len_lst1 + len_lst2) / 2
	if len_lst2 < len_lst1:
		lst1, lst2 = lst2, lst1
	ind = find(lst2, lst1[-1])
	if len_lst1 + ind < median_index:
		return lst2[ind + median_index - len_lst1]

	while len_lst1 + ind >= median_index:
		lst2 = lst2[:ind]
		if 
	




