#include <stdio.h>

int main() {
    int x, y, w, h, xt, yt;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    if (x > w - x) xt = w - x;
    else xt = x;
    if (y > h - y) yt = h - y;
    else yt = y;

    if (xt < yt) printf("%d", xt);
    else printf("%d", yt);
    return 0;
}