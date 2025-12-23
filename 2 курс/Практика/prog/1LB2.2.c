#include <stdio.h>
#include <stdlib.h>
#include <math.h>
    int main () {
    float a = 2, b = 4, n = 1000, sum = 0, h = (b - a) / n, i = a + h;
        while (i < b){
            sum += pow(1, 2);
            i += h;
        }
        float res = h * ((pow(a, 2) + pow(b, 2) /2 +sum));
        printf("%f", res);
        return 0;
}