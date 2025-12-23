#include <stdio.h>

int main () {
    int s = 3, M[3][3] = {1,2,3,4,5,6,7,8,9};
    for (int i = 0; i < s; ++i) {
        int sum = 0;
        for (int j = 0; j < s; ++j) {
            sum +=M[i][j];
        }
        M[i][0] = sum / s;
    }
    for (int i = 0; i < s; ++i) {
        for (int j = 0; j < s; ++j) {
            printf("%d", M[i][0]);
        }
        printf("\n");
    }
    return 0;
}