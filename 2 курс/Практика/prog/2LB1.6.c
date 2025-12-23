#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 1234567890;
    int *intPtr = &a;
    char *p;
    p = (char *)intPtr;
    printf("%d \n\n", *intPtr);
    for (int i = 0; i < sizeof(int); i++){
        printf("%d \n", *p);
        p++;
    }
    return 0;
}