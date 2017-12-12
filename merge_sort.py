def merge_sort(a, p, r):
	if p < r:
		q = int((r + p) / 2)
		merge_sort(a, p, q)
		merge_sort(a, q + 1, r)
		merge(a, p, q, r)

def merge(a, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	ll = a[p:q + 1]
	rl = a[q + 1: r + 1]
	i = 0
	j = 0
	for k in range(p, r + 1):
		if i == n1:
			a[k:r+1] = rl[j::]
			break
		if j == n2:
			a[k:r+1] = ll[i::]
			break
		if ll[i] <= rl[j]:
			a[k] = ll[i]
			i += 1
		else:
			a[k] = rl[j]
			j += 1
		# if i == n1 or j == n2:
		# 	if i == n1:
		# 		a[k] = rl[j]
		# 		j += 1
		# 	elif j == n2:
		# 		a[k] = ll[i]
		# 		i += 1
		# else:
		# 	if ll[i] <= rl[j]:
		# 		a[k] = ll[i]
		# 		i += 1
		# 	else:
		# 		a[k] = rl[j]
		# 		j += 1

a = [5,2,4]

merge_sort(a, 0, len(a) - 1)

print(a)