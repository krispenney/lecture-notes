#include <unistd.h>
#include <stdio.h>

int main(){
    printf("B\n");
    fork();
    printf("C\n");
    fork();
    printf("D\n");
    fork();
    return 0;
}
