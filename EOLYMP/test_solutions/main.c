#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double dist(int x1, int y1, int x2, int y2)
{
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

int intersect(int x1, int y1, int r1, int x2, int y2, int r2)
{
    double d = dist(x1, y1, x2, y2);

    if (d > r1 + r2)
        return 0;
    else if (d < abs(r1 - r2))
        return 0;
    else if (d == 0 && r1 == r2)
        return -1;
    else if (d == r1 + r2 || d == abs(r1 - r2))
        return 1;
    else
        return 2;
}

int main() {
    int a, b, c, d, e, f;
    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    printf("%d\n", intersect(a, b, c, d, e, f));
}
