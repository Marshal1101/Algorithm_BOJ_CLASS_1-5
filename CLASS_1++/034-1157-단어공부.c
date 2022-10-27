#include <stdio.h>

int main() {
    int i, len, alphabet[26], max = 0, max_Idx, cnt = 0;
    for (i = 0; i < 26; i++) {
        alphabet[i] = 0;
    }
    char input[1000001];
    scanf("%s", input);
    len = strlen(input);
    for (i = 0; i < len; i++) {
        if (input[i] < 91) {
            alphabet[input[i] - 65] += 1;
        } else {
            alphabet[input[i] - 97] += 1;
        }
    }
    for (i = 0; i < 26; i++) {
        if (alphabet[i] > max) {
            max = alphabet[i];
            max_Idx = i;
        }
    }
    for (i = 0; i < 26; i++) {
        if (alphabet[i] == max) {
            cnt++;
            if (cnt > 1) break;
        }
    }
    if (cnt < 2) printf("%c", max_Idx + 65);
    else printf("?");
}