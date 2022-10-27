#include <stdio.h>
#include <string.h>

int main() {
	int n, m;
	char a[21];
	scanf("%d", &n);
	while (n-- > 0)
	{
		scanf("%d %s", &m, a);
		for (int i = 0; i < strlen(a); i++)
			for (int j = 0; j < m; j++)
				printf("%c", a[i]);
		printf("\n");
	}
	return 0;
}