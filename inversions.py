#program to count the inversions in an array
import math
def inversions(lo, hi):
	global lst
	if hi - lo < 2:
		return 0

	res = 0
	mid = lo + math.floor((hi - lo - 1) / 2)
	res += inversions(lo, mid+1)
	#print(res)
	res += inversions(mid+1, hi)
	#print(res)
	a = lo
	c = mid+1
	new = []
	while a <= mid and c < hi:
		if lst[c] < lst[a]:
			new.append(lst[c])
			c += 1
			res += (mid - a + 1)
		else:
			new.append(lst[a])
			a += 1
	if a > mid:
		for i in range(c, hi):
			new.append(lst[i])
	else:
		for i in range(a, mid+1):
			new.append(lst[i])
	for i in range(lo, hi):
		lst[i] = new[i-lo]
	return res

lst = [2,6,4,1,4]
print(inversions(0,len(lst)))
