def maximal_subarray_sum (lst):
	c = 0
	ans = 0
	for i in range(len(lst)):
		c += lst[i]
		ans = max(ans,c)
		if c < 0:
			c = 0
	print("maximal subarray sum is :", ans)

lst = [4,-5,2,1]
maximal_subarray_sum(lst)
lst = [4,-5,2,4]
maximal_subarray_sum(lst)


