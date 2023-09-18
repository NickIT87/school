#include <stdio.h>

short int solver (short int);

int main()
{
    short int y = 0;
    scanf("%hd", &y);
    printf("y = %hd\n", solver(y));
    return 0;
}

short int solver (short int x)
{
    if (x < 5) 
        return x * x - 3 * x + 4;
    else
        return x + 7;
}