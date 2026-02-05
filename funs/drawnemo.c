#include<stdio.h>
#include<windows.h>
void main(){
    SetConsoleOutputCP(CP_UTF8);
    int width,height,i,j;
    if(i<2||j<2){
        printf("print error");
        return;
    }
    scanf("%d %d",&width,&height);
    for(i=0;i<height;i++){
        for(j=0;j<width;j++){
            if(i==0&&j==0) printf("┌");
            else if(i==0&&j==width-1) printf("┐");
            else if(i==height-1&&j==0) printf("└");
            else if(i==height-1&&j==width-1) printf("┘");
            else if(i==0||i==height-1) printf("─");
            else if(j==0||j==width-1) printf("│");
            else printf(" ");
        }
        if(i!=height-1) printf("\n");
    }
}