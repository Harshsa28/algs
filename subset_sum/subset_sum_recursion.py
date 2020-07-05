def subset_sum(lst, c):
	if c == 0:
		print("yes!!")
		import sys
		sys.exit()
		return
	if len(lst) == 0:
		return
	subset_sum(lst[:len(lst)-1], c-lst[-1])
	subset_sum(lst[:len(lst)-1], c)
	return


def solve(lst,c):
	subset_sum(lst,c)
	print("no")
	return

x = [i for i in range(10)]
solve(x, 10)
