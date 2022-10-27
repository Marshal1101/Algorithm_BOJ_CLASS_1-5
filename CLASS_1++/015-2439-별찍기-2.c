#include <stdio.h>
int main() {
    int N, i, j, k;
    scanf("%d", &N);
    for (i = 1; i < N+1; i++) {
        for (j = 0; j < N-i; j++) {
            printf(" ");
        }
        for (k = 0; k < i; k++) {
            printf("*");
        }
        printf("\n");
    }
}