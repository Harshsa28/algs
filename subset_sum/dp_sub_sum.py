#solve subset sum problem in pseudo polynomial time using Dynamic Programming
#prints 1 if there is a subset sum, 0 otherwise

dp = {}

def dp_sub_sum(lst, i, c):
	global dp
	if (i,c) in dp:
		return dp[(i,c)]
	elif c == 0:
		dp[(i,c)] = 1
	elif i == 0:
		dp[(i,c)] = 0		
	elif lst[i] > c:
		if (i-1, c) in dp:
			dp[(i, c)] = dp[(i-1, c)]
		else:
			dp[(i,c)] = dp_sub_sum(lst, i-1, c)
	else:
		dp[(i,c)] = dp_sub_sum(lst, i-1, c) or dp_sub_sum(lst, i-1, c-lst[i])
	return dp[(i,c)]


def solve(lst, c):
	global dp
	print(dp_sub_sum(lst, len(lst)-1, c))
	print(dp)
	return

x = [i for i in range(10)]

solve(x, 14)

