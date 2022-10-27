#include<stdio.h>
int n[11];
int main() {
	int a, s = 1, i;
	for (i = 0; i < 3 ; i++) {
		scanf("%d", &a);
		s *= a;
	}
	while (s) {
		n[s%10]++;
		s /= 10;
	}
	for (i = 0; i < 10; i++) {
		printf("%d\n", n[i]);
	}
}