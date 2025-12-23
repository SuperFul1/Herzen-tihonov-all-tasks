#include <stdio.h>

int main () {
    int x = 8, y[8] = {1,2,3,4,5,6,7,8}, b;
    for (int i = 1; i < x; ++i) {
        for (int j = i; j > 0 && y[j] < y[j - 1]; --j) {
            b = y[j - 1];
            y[j - 1] = y[j];
            y[j] = b;
        }
    }
    for (int i = 0; i < x; ++i) {
        printf("%d", y[i]);
    }
    return 0;
}