#include<stdio.h>
#if defined(_WIN32)||defined(_WIN64)
    #include<windows.h>
#endif
int main(){
    #if defined(_WIN32)||defined(_WIN64)
        SetConsoleOutputCP(CP_UTF8);
    #endif
    int width,height,i,j;
    scanf("%d %d",&width,&height);
    if(width<2||height<2){
        printf("cannot print\n");
        return 1;
    }
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
    return 0;
}