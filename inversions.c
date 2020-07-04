// C program to count inversions in an array

#include <stdio.h>
#include <math.h>

int lst[6] = {2,6,4,1,4,10};

int inversions(int lo, int hi){
	if ((hi - lo) < 2){
		return 0;
	}
	int res = 0;
	int mid = lo + ((hi - lo - 1)/2);
	int a = lo;
	int c = mid+1;
	res += inversions(lo, mid+1);
	res += inversions(mid+1, hi);
	int length = (hi - lo);
	int new[length];
	int new_index = 0;
	while (a <= mid && c < hi){
		if (lst[c] < lst[a]){
			new[new_index++] = lst[c++];
			res += (mid - a)+1;
		}
		else{
			new[new_index++] = lst[a++];
		}
	}

	if (a > mid){
		for (int i = c; i != hi; ++i){
			new[new_index++] = lst[i];
		}
	}
	else{
		for (int i = a; i <= mid; ++i){
			new[new_index++] = lst[i];
		}
	}
	for (int i = lo; i < hi; ++i){
		lst[i] = new[i-lo];
	}
	return res;
}

int main(){
	int len_lst = sizeof(lst)/sizeof(lst[0]);	
	int inv = inversions(0, len_lst);
	printf("number of inversions is :%d\n", inv);
	return 0;
}

