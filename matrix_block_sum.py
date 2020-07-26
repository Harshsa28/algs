def integral_image (matrix):
	n = len(matrix)
	m = len(matrix[0])
	image = [[0 for i in range(n+1)] for j in range(m+1)]
	#image[0][0] = matrix[0][0]
	#image[0][1] = matrix[0][0] + matrix[0][1]
	#image[1][0] = matrix[0][0] + matrix[1][0]
	for i in range(n):
		for j in range(m):
			image[i+1][j+1] = image[i+1][j] + image[i][j+1] - image[i][j] + matrix[i][j]
	print(image)
	return image #image i and j are increased by 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#integral_image(matrix)


def block_sum (matrix, k):
	image = integral_image (matrix)
	n = len(matrix)
	m = len(matrix[0])
	ans = [[0 for i in range(n)] for j in range(m)]
	for i in range(n):
		for j in range(m):
			r1 = max(0, i-k)
			r2 = min(n-1, i+k)
			c1 = max(0, j-k)
			c2 = min(m-1, j+k)
			ans[i][j] = image[r2+1][c2+1] - image[r1][c2+1] - image[r2+1][c1] + image[r1][c1]
	print(ans)

block_sum (matrix, 2)
