#include <stdio.h>

int main() {
    int n, len, total = 0;
    char input[100];
    scanf("%d", &n);
    scanf("%s", input);
    for (int i = 0; i < n; i++) {
        total += input[i] - 48;
    }
    printf("%d", total);
}