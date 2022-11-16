
/*
Pseudocode:

FUNCTION factorial(n):
    Let R equal 1
    for i=n down to 1 do
        R = R*i
    return R

#include <iostream>
#include <string>
using namespace std;
int main(){
    int n;
    cin >> n;
    cout<<factorial(n);

    return 0;
}
*/


int factorial(int n){
    int r = 1;
    for (int i=n; i>1; --i) r = r*i;
    return r;
}

