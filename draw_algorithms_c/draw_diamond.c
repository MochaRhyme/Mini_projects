#include<stdio.h>
int main(){
    int i,j,h,b;
    printf("Input height of diamond : ");
    scanf("%d",&h);
    if(h%2==0){
        printf("DIAMOND CANNOT BE EVEN HEIGHT\n");
        return 1;
    }
    b=h/2+1;
    for(i=0;i<h;i++){
        if(i<b){
            for(j=0;j<b-1-i;j++) printf(" ");
            for(j=0;j<2*i+1;j++) printf("*");
        }else{
            for(j=0;j<i-b+1;j++) printf(" ");
            for(j=0;j<2*h-2*i-1;j++) printf("*");
        }
        printf("\n");
    }
}