def quick_sort(a, p, r):
	if p < r:
		q = partition(a, p, r)
		quick_sort(a, p, q - 1)
		quick_sort(a, q + 1, r)

def partition(a, p, r):
	x = a[r]
	i = p
	for j in range(p, r):
		if x > a[j]:
			m = a[i]
			a[i] = a[j]
			a[j] = m
			i += 1
	a[r] = a[i]
	a[i] = x
	return i

a = [9,2,8,7,1,3,9]

quick_sort(a, 0, len(a) - 1)

print(a)