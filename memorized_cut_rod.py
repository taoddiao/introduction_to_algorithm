def memorized_cut_rod(p, n):
	r = dict()
	for i in range(0, n + 1):
		r[i] = -1
	return memorized_cut_rod_aux(p, n, r)

def memorized_cut_rod_aux(p, n, r):
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = 0
	else:
		q = -1
		for i in range(1, n + 1):
			q = max(q, p[i] + memorized_cut_rod_aux(p, n - i, r))
	r[n] = q
	return q

p = {0:0, 1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

for i in range(11):
	print(memorized_cut_rod(p, i))