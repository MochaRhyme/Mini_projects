#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
void swapIntVar(int* a,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void reverseIntArray(int* arr,int len){
    for(int i=0;i<len/2;i++){
        swapIntVar(&arr[i],&arr[len-1-i]);
    }
}
int collectRand(int start,int end){
    return rand()%(end-start+1)+start;
}
int main(){
    srand((unsigned int)time(NULL));
    for(int i=0;i<50;i++){
        printf("%d\n",collectRand(2,4));
    }
}