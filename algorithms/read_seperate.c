#include<stdio.h>
#include<wchar.h>
#include<locale.h>
#if defined(_WIN32) || defined(_WIN64)
    #include <windows.h>
    #define DELAY(ms) Sleep(ms)
#elif defined(__linux__) || defined(__unix__) || defined(__APPLE__)
    #include<unistd.h>
    #define DELAY(ms) usleep((ms)*1000)
#else
    #warning "Unsupported OS"
    #define DELAY(ms)
#endif

void seperatePrint(wchar_t* line){
    for(int i=0;i<wcslen(line);i++){
        wprintf(L"%lc",line[i]);
        fflush(stdout);
        if(line[i]==L','){
            DELAY(200);
        }else{
            DELAY(50);
        }
    }
}

int main(){
    setlocale(LC_ALL,"");
    seperatePrint(L"Follow the white rabbit");
    wprintf(L"\n");
    DELAY(3000);
    seperatePrint(L"죽느냐 사느냐, 그것이 문제로다.");
    wprintf(L"\n");
    return 0;
}