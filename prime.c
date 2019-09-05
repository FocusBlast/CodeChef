#include <stdio.h>
main(){
    int a;
    scanf("%d", &a);
    if(a%1==0 && a%a==1){
        printf("prime");
    }
    else{
        printf("odd");
    }
}