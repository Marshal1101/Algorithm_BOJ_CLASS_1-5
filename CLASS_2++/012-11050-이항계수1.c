#include <stdio.h>

int main() {
    int n, k, i, res;
    scanf("%d %d", &n, &k);
    res = (factorial(n, k) / factorial(k, k));
    printf("%d", res);
    return 0;
}

int factorial(num, k) {
    int i, j, total = 1;
    i = num;
    j = k;
    while (j > 0 ) {
        total *= i--;
        j--;
    }
    return total;
}