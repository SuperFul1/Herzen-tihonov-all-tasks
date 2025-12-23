#include <stdio.h>
#include <stdlib.h>

struct list {
    int field;
    struct list *next;
    struct list *prev;
};

struct list * init(int a) {
    struct list *lst;
    lst = (struct list*)malloc(sizeof(struct list));
    lst->field = a;
    lst->next = NULL;
    lst->prev = NULL;
    return(lst);
}

void NewNode(struct list *lst, int number) {
    struct list *temp, *p;
    temp = (struct list*) malloc(sizeof(struct list));
    p = lst->next;
    lst->next = temp;
    temp->field = number;
    temp->next = p;
    temp->prev = lst;
    if (p != NULL){
        p->prev = temp;
    }
}

struct list * tail(struct list *lst){
    struct list *res = lst;
    while (res->next != NULL ){
        res = res->next;
    }
    return (res);
}

void purge(struct list *lst){
    while (lst->next != NULL ){
        lst = lst->next;
        free(lst->prev);
    }
    free(lst);
}

int main(void) {
    int value;
    int n = 5;
    scanf("%i",&value);
    struct list* a = init(value);
    struct list* p = a;
    for(int i = 0; i < n-1; i++){
        scanf("%i",&value);
        NewNode(p, value);
        p = p->next;
    }
    p = a;
    for(int i = 0; i < n; i++){
        printf("%i ",p->field);
        p = p->next;
    }
    printf("\n");
    p = tail(a);
    for(int i = 0; i < n; i++){
        printf("%i ",p->field);
        p = p->prev;
    }
    purge(a);
    return 0;
}