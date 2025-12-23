#include <stdio.h>
#include <math.h>
    int main (){

        int sum = 11;
        while (sum > 10)
        {
            int num= 0;
            printf("num:");
            scanf("%d, &num");
            sum = (num / 100) + (num / 100 / 10) + fmod(num, 10.0);

        }
}
