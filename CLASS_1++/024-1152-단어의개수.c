#include <unistd.h>
#include <stdio.h>

int main(void)
{
    int count;
    char str[1000005];
    int i;

    i = 0;
    count = 0;
    read(0, str, 1000005);
    if (str[i] == ' ')
        i++;
    if (str[i] && str[i] != '\n')
        count = 1;
    while (str[i])
    {
        if ((str[i] == ' ') && (str[i + 1] != 0) && str[i + 1] != '\n')
            count++;
        i++;
    }
    printf("%d", count);
    return (0);
}