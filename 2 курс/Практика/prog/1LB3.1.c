#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main (){
    int c;
    printf("elemets vector:");
    scanf("%d", &c);
    int vect[c];
    int num;
    for (int i = 0; i < c; ++i){
        printf("vvedite elemets:");
        scanf("%d", &num);
        vect [i] = num;
    }
    printf("novii vector: ");
    for (int i = 0; i < c; ++i){
        vect[i] *= vect[i];
        printf("%d", vect[i]);
    }
    return 0;
}