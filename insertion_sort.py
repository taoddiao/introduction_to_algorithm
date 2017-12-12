def insertion_sort(a):
	for i in range(1, len(a)):
		j = i - 1
		key = a[i]
		while a[j] > key and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	return
