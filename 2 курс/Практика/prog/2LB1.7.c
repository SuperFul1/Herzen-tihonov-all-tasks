#include <stdio.h>
#include <stdlib.h>

int main() {
    char **arr = NULL;
    int i, n;
    scanf("%d", &n);

    arr = (char **)malloc(sizeof(char *) * n);

    for (i = 0; i<n; i++) {
        char *s;
        arr[i] = (char*)malloc(1024);
        arr[i][0] = '\0';
        scanf("%s", arr[i]);
    }

    for (i =0; i < n; i++){

        printf("%s \n", arr[i]);
        free(arr[i]);
    }
    free(arr);
    return 0;
}