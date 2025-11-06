#include<stdio.h>
#include<stdbool.h>

bool isPrimeNumber(int num){
    for(int i=2;i<num;i++){
        if(num%i==0){
            return false;
        }
    }
    return true;
}