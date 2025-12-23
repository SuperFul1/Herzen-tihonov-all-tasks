#include <stdio.h>
    int P( int x) {
        if (x == 0) return 1;
        else if (x == 1) return 1;
        else if (x == 2) return 1;
        else return (P(x - 2) + P(x - 3));

}

    int main () {

    int u;
        printf("u:");
        scanf("%d", &u);
        for (int i = 0; P(i) <=u; i++)
        {
            printf("%d", P(i));
        }
}