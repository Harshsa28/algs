import math
def maj_ele(lst):
	count = 0
	cand = 0
	for i in range(len(lst)):
		if count == 0:
			cand = i
			count = 1
		elif lst[i] == lst[cand]:
			count += 1
		else:
			count -= 1
	
	count = 0

	for i in range(len(lst)):
		if lst[i] == lst[cand]:
			count += 1
	
	if count > math.floor(len(lst)/2):
		print("majority ele is :", lst[cand])
	else:
		print("no majorit ele")
	return

lst = [1,2,1,3,1,4,1]
maj_ele(lst)
lst = [2,3,3,3,1,1,3]
maj_ele(lst)
