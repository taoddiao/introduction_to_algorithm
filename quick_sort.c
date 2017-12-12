#include <stdio.h>

void quick_sort(int *, int, int);

int partition(int *, int, int);

void quick_sort(int *a, int p, int r)
{
	if(p < r) 
	{
		int q = partition(a, p, r);
		quick_sort(a, p, q - 1);
		quick_sort(a, q + 1, r);
	}
}

int partition(int *a, int p ,int r)
{
	int x = a[r];
	int i = p - 1;
	int m;
	for (int j = p; j < r; ++j)
	{
		if(a[j] <= x){
			i++;
			m = a[i];
			a[i] = a[j];
			a[j] = m;
		}
	}
	a[r] = a[i + 1];
	a[i + 1] = x;
	return i + 1;
}

int main(void)
{
	int a[] = {9,2,8,7,1,3,9,0};
	quick_sort(a, 0, 7);
	for (int i = 0; i < 8; ++i)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}