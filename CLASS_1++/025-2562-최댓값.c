#include <stdio.h>

int main() {
	int num, max_i;
    int max = 0;
    int i = 1;
	while(scanf("%d", &num) != -1) {
        if (num > max) {
            max = num;
            max_i = i;
        }
        i++;
    }
    printf("%d\n%d", max, max_i);
}