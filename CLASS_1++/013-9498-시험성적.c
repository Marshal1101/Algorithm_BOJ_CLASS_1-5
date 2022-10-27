#include <stdio.h>
int main() {
    int point;
    scanf("%d", &point);
    if (point >= 90) printf("A");
    else if (point >= 80) printf("B");
    else if (point >= 70) printf("C");
    else if (point >= 60) printf("D");
    else printf("F");
}