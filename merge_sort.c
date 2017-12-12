#include <stdio.h>

void merge_sort(int *, int, int);
void merge(int *, int, int, int);

void merge_sort(int *a, int p, int r)
{
	if(p < r)
	{
		int q = (r + p) / 2;
		merge_sort(a, p, q);
		merge_sort(a, q + 1, r);
		merge(a, p, q, r);
	}
}

void merge(int *a, int p, int q, int r)
{
	int n1 = q - p + 1;
	int n2 = r - q;
	int ll[n1];
	int rl[n2];
	for(int i = 0; i < n1; i++)
	{
		ll[i] = a[p + i];
	}
	for(int j = 0; j < n2; j++)
	{
		rl[j] = a[q + 1 + j];
	}
	int i = 0;
	int j = 0;
	for(int k = p; k <= r; k++)
	{
		if(i == n1 or j == n2)
		{
			if(i == n1)
			{
				a[k] = rl[j];
				j++;
			}else
			{
				a[k] = ll[i];
				i++;
			}
		}else
		{
			if(ll[i] <= rl[j])
			{
				a[k] = ll[i];
				i++;
			}else
			{
				a[k] = rl[j];
				j++;
			}
		}
	}
}

int main(void)
{
	int a[8] = {5,2,4,7,1,3,2,6};
	merge_sort(a, 0, 7);
	for (int i = 0; i < 8; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}