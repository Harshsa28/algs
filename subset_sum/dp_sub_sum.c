#include <stdio.h>

int solve(int arr[], int n, int c){
	int dp[n+1][c+1];
	for (int i = 0; i < n+1; ++i){
		dp[i][0] = 1;
	}
	for (int i = 1; i < c+1; ++i){
		dp[0][i] = 0;
	}
	for (int i = 1; i <= n; ++i){
		for (int j = 1; j <= c; ++j){
			if (j < arr[i-1]){
				dp[i][j] = dp[i-1][j];
			}
			else{
				dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]]) % 2;
			}
		}
	}
	for (int i = 0; i <= n; ++i){
		for (int j = 0; j<= c; ++j){
			printf("%d ", dp[i][j]);
		}
		printf("\n");
	}
	return dp[n][c];
}

int main(){
	int arr[10];
	for (int i= 0; i < 10; ++i){
		arr[i] = i;
	}
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("n is %d\n", n);
	int c = 45;
	printf("ans is %d\n", solve(arr, n, c));
	return 0;
}

