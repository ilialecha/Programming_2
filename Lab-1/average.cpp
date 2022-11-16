#include <iostream>
#include <iomanip>

using namespace std;
/*
'''
procedure average(L)
    let n be |L|
    let r be an integer
    for i=1 up to n do
        r = r + L[i]
    output r/n

'''
*/

void average(){
    double r = 0;
    int i = 0;
    double in;
    while(cin>>in){
        r = r+in;
        i++;
    }
    printf("%.2f\n",r / i);
}


int main(){
    average();
    return 0;
}