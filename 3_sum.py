	def three_sum(lst, c):
		soln = []
		lst.sort()
		for i in range(len(lst)):
			j = i+1
			k = len(lst)-1
			while j < k:
				if (lst[j] + lst[k] == c-lst[i]):
					temp = [lst[i],lst[j],lst[k]]
					if temp not in soln:
						soln.append(temp)
					j += 1
					k -= 1
				elif lst[j] + lst[k] < c-lst[i]:
					j += 1
				else:
					k -= 1
		print(soln)
		return

	def solve(lst):
		three_sum(lst, 0)

x = [-1,0,1,2,-1,4]
solve(x)
