#include <stdio.h>

int main(void)
{
	int i,n,temp,max,min;
	scanf("%d",&n);
	scanf("%d",&temp);
	max=temp;
	min=temp;
	for(i=0;i<n-1;i++)
	{
		scanf("%d",&temp);
		if(temp>max)
			max=temp;
		if(temp<min)
			min=temp;
	}
	printf("%d %d",min,max);

	return 0;
}