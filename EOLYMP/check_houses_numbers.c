#include <stdio.h>
/*
Determine if the houses with numbers n and m 
are located on one side of the street.
Input data 
Two numbers n and m (1 ≤ n, m ≤ 100).
Output data
Print 1 if the houses with numbers n and m 
are located on one side of the street and 0 otherwise.
*/
short check_houses_numbers(short n, short m)
{
    if ((n % 2 == 0 && m % 2 == 0) || 
        (n % 2 != 0 && m % 2 != 0))
        return 1;
    else
        return 0;
}

int main()
{
    printf("%hd\n", check_houses_numbers(1, 3));
    return 0;
}