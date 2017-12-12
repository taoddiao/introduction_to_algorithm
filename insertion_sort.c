
void insertion_sort(int *, int);

void insertion_sort(int *a, int n){
	int key;
	int j;
	for (int i = 1; i < n; i++){
		j =  i - 1;
		key = a[i];
		while (key < a[j] and j >= 0){
			a[j + 1] = a[j];
			j--;
		}
		a[j + 1] = key;
	}

}

int main(void){

	return 0;
}