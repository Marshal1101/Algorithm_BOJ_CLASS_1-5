#include <stdio.h>

int main() {
    int t, i, total, cnt;
    char res[81];
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%s", res);
        total = cnt = 0;
        for (int j = 0; j < strlen(res); j++) {
            if (res[j] == 'O') {
                total += ++cnt;
            } else cnt = 0;
        }
        printf("%d\n", total);
    }
}

// 문자열 따옴표 "O" (x) => 'O' (o)