def array_rotation (lst, hm):
	if hm >= len(lst):
		hm = hm % len(lst)
	lst1 = lst[0:hm]
	lst2 = lst[hm:]
	lst3 = lst2 + lst1
	return lst3

print(array_rotation([1,2,3,4,5],0))
