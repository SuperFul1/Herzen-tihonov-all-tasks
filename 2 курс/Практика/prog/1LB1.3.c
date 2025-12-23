#include <math.h>
#include <stdio.h>
    int main () {
        float x, y, sum, u;
        printf("vvedite x=");
        scanf("%f", &x);
        printf("vvedite y= ");
        scanf("%f", &y);
        sum = abs(sin (x + y));
        u = (1 + pow(sum, 2)) / (2 + abs(x - (2 * pow(x, 2)) / (1 - sum)));
        printf("s(%f, %f)= %f", x, y, u);
        return 0;




}
