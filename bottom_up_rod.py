def bottom_up_cut_rot(p, n):
	r = dict()
	r[0] = 0
	for j in range(1, n + 1):
		q = -1
		for i in range(1, j + 1):
			q = max(q, p[i] + r[j - i])
		r[j] = q

	return r[n]

def extended_bottom_up_cut_rod(p, n):
	r = dict()
	s = dict()
	r[0] = 0
	s[0] = 0
	for j in range(1, n + 1):
		q = -1
		for i in range(1, j + 1):
			if q < p[i] + r[j - i]:
				q = p[i] + r[j - i]
				s[j] = i
		r[j] = q

	return r,s

def print_cut_rot_solution(p, n):
	_, s = extended_bottom_up_cut_rod(p, n)
	while n > 0:
		print(s[n])
		n -= s[n]

p = {0:0, 1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

r,s = extended_bottom_up_cut_rod(p, 10)

for key in r.keys():
	print(r[key], s[key])

print_cut_rot_solution(p, 7)