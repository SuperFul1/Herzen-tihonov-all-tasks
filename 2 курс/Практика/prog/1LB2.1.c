#include <math.h>
#include <stdio.h>
    int main () {
        long int r1 = 228000000, r2 = 149600000, x, y;
        double T1 = 364.25, T2 = 687, w1 = 2 * M_PI / T1, w2 = 2 * M_PI / T2;
        for (int (t) = 1; (t) < 31; t ++) {
            x = r1 * cos(w1 * t) - r2 * cos(w2 * t);
            y = r1 * sin(w1 * t) - r2 * sin(w2 * t);
            printf("%d (%li, %li) (km\\day)\n", t, x, y);

        }
    return 0;
}