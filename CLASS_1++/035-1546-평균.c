#include <stdio.h>
int main() {
    int n, m, i, x = 0;
    double s = 0;
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        scanf("%d", &m);
        s += m;
        if(m > x) x = m;
    }
    printf("%lf", s/x*100/n);
}