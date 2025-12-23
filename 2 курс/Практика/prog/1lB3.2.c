#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main (){
    int len;
    printf("massive");
    scanf("%d", &len);
    int m[len], i;
    for (int i = 0; i < len; ++i) {
        printf("m[%d] = ", i);
        scanf("%d", &m[i]);
    }
    printf("your massive:");
    for (int i = 0; i < len; ++i){
        printf("%d", m[i]);
    }
    int j;
    printf("revers massive:");
    for (int j = len - 1; j>=0; j--) {
        printf("%d", m[j]);
    }
    return 0;
}