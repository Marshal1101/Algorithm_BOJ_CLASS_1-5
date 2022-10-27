#include <stdio.h>

int main() {
    int i, j, len, alphabet[26];
    for (i = 0; i < 26; i++) {
        alphabet[i] = -1;
    }
    char input[100];
    scanf("%s", input);
    len = strlen(input);
    for (i = 0; i < 26; i++) {
        for (j = 0; j < len; j++) {
            if (input[j] - 97 == i) {
                alphabet[i] = j;
                break;
            }
        }
    }

    for (i = 0; i < 26; i++) {
        printf("%d ", alphabet[i]);
    }
}