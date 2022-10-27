#include<stdio.h>

int tree[27][2], a, b, c, n;

void f(int v, int n)
{
  if(v == '.') return;
  if(n == 2) printf("%c", v);
  f(tree[v][0], n);
  if(n == 1) printf("%c", v);
  f(tree[v][1], n);
  if(n == 0) printf("%c", v);
}

int main(void)
{
  scanf("%d", &n);
  while(n--)
  {
    scanf(" %c %c %c", &a, &b, &c);
    tree[a][0] = b;
    tree[a][1] = c;
  }
  n = 3;
  while(n--)
  {
    f('A', n);
    printf("\n");
  }
  
  return 0;
}