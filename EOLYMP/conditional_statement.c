#include <stdio.h>
#include <math.h>

short int solver (short int);
short int solver2 (short int);

int main()
{
    short int y = 0;
    scanf("%hd", &y);
    //printf("y = %hd\n", solver(y));
    printf("y = %hd\n", solver2(y));
    return 0;
}

short int solver (short int x)
{
    if (x < 5) 
        return x * x - 3 * x + 4;
    else
        return x + 7;
}

short int solver2 (short int x)
{
    if (x >= 10) 
        return pow(x, 3) + 5 * x;
    else
        return x * x - 2 * x + 4;
}