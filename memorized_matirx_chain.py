def memorized_matrix_chain(p):
	n = len(p) - 1
	m = [[float('inf') for j in range(n + 1)] for i in range(n + 1)]

	return lookup_chain(m, p, 1, n)


def lookup_chain(m, p, i, j):
	if m[i][j] < float('inf'):
		return m[i][j]
	if i == j:
		m[i][j] = 0
	else:
		for k in range(i, j):
			q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
			if q < m[i][j]:
				m[i][j] = q
	return m[i][j]


p = [30, 35, 15, 5, 10, 20, 25]

print(memorized_matrix_chain(p))