#include <math.h>
#include <stdio.h>
int main () {
    float a = 0.27, b = 3.9, c = 2.8, x = 1.8, h;
    h = - ((x - a) / (cbrt(pow(x, 2) + pow(a, 2)))) - ((4 * sqrt(sqrt(pow(pow(x, 2) + pow(b, 2), 3)))) / (2 + a + b +
                                                                                                          cbrt(pow(x - c, 2))));
    printf("h(%f) = %f", x, h);

}
