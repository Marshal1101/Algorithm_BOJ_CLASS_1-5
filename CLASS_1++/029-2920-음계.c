#include <stdio.h>

int main() {
    int num, i, asc = 1, desc = 1, mixed = 1;

    for (i = 1; i < 8; i++) {
        scanf("%d", &num);
        if (num != i) {
            asc = 0;
        }

        if (num != 9-i) {
            desc = 0;
        }
    }

    if (asc == 1) printf("ascending");
    else if (desc == 1) printf("descending");
    else printf("mixed");
}