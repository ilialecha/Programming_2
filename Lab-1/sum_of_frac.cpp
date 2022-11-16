#include <iostream>
#include <iomanip>

using namespace std;

void sum_of_frac(int a,int b,int k){
    float r = 0.0;
    int i = 0;
    if (k!=0 && a!=0 && b!=0){
        while ( (a+(i*k)) <= b){
            r = r + ((float) 1/(a+(i*k)) );
            i++;
        }
    }
    
    printf("%.4f\n",r);
}

int main(){

    int a,b,k;

    while(cin>>a>>b>>k) sum_of_frac(a,b,k);

    return 0;
}