#include <stdio.h>

int main() {
    int num, i, rest[42], cnt = 0;
    for (i = 0; i < 42; i++) {
        rest[i] = 0;
    }
    for (i = 0; i < 10; i++) {
        scanf("%d", &num);
        rest[num % 42] = 1;
    }
    for (i = 0; i < 42; i++) {
        if (rest[i] == 1) cnt++;
    }
    printf("%d", cnt);
}