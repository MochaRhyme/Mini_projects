#include<stdio.h>
#include<math.h>
void swapInt(int* a,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void reverseIntArray(int* arr,int len){
    for(int i=0;i<len/2;i++){
        swapInt(&arr[i],&arr[len-1-i]);
    }
}

int main(){
    
}