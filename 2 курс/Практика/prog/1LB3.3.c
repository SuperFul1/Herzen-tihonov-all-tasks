#include <stdio.h>

int main (){
    int s = 3, m1[3][3] = {1,2,3,4,5,6,7,8,9};
    int m2[s][s];
    for (int i = 0; i < s; ++i) {
        for (int j = 0; j < s; ++j) {
            m2[j][i] = m1[i][j];
        }
    }
    for (int i = 0; i < s; ++i) {
        for (int j = 0; j < s; ++j) {
            printf("%d", m2[i][j]);
        }
        printf("\n");
    }
    return 0;
}