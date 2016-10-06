#include <unistd.h>
#include <stdio.h>

int x;
int main(){
    int rc;
    x = 0;
    rc = fork();
    if(rc == 0){
        x = 10;
        printf("A: %d\n", x);
    }else{
        printf("B: %d\n", x);
        x = 100;
    }
    printf("C: %d\n", x);
}

