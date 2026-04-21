#include<stdio.h>
int main(){
    int i,j,h;
    printf("Input height of stair : ");
    scanf("%d",&h);
    for(i=1;i<=h;i++){
        for(j=i;j>0;j--) printf("%d",j);
        for(j=2;j<=i;j++) printf("%d",j);
        printf("\n");
    }
    return 0;
}