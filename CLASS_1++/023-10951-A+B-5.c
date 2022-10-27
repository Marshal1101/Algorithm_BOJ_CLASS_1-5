#include <stdio.h>

int main() {
	int a = 0;
    int b = 0;
    scanf("%d %d", &a, &b);
	while (a != 0) {
		printf("%d\n", a + b);
    	scanf("%d %d", &a, &b);
	}
}