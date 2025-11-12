#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>


// 부품 함수
void swapIntVar(int* a,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
int literalRand(int o1,int o2){
    return rand()%o1+o2;
}
int collectRand(int start,int end){
    return literalRand(end-start+1,start);
}

// 실제 구현 함수
void rIA(int* arr,int len){
    for(int i=0;i<len/2;i++){
        swapIntVar(&arr[i],&arr[len-1-i]);
    }
}
void rfIA(int* arr,int len,int start,int end){
    for(int i=0;i<len;i++){
        arr[i]=collectRand(start,end);
    }
}
void pIA(int* arr,int len,char* sep,char* end){
    for(int i=0;i<len;i++){
        printf("%d",arr[i]);
        if(i!=len-1){
            printf("%s",sep);
        }
    }
    printf("%s",end);
}

#define reverseIntArray(a) rIA(a,sizeof(a)/sizeof(int))
#define randomfillIntArray(a,s,e) rfIA(a,sizeof(a)/sizeof(int),s,e)
#define printIntArray(a,s,e) pIA(a,sizeof(a)/sizeof(int),s,e)

// 실행부
int main(){
    srand((unsigned int)time(NULL));
    int a[]={12,23,34,45};
    printIntArray(a," ","\n");
    reverseIntArray(a);
    printIntArray(a," ","\n");
}