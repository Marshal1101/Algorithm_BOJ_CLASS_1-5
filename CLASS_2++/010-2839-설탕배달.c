#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int bag[n+1];
    for (int i = 0; i < n+1; i++) {
        bag[i] = 5001;
    }
    bag[0] = 0;
    for (int i = 0; i < n+1; i++) {
        bag[i+3] = (bag[i] + 1 > bag[i+3] ? bag[i+3] : bag[i] + 1);
        bag[i+5] = (bag[i] + 1 > bag[i+5] ? bag[i+5] : bag[i] + 1);
    }
    if (bag[n] < 5001) printf("%d", bag[n]);
    else printf("-1");
}