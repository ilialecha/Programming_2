#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

void HANOI(int n, char left, char middle, char right){
    if ( n > 0 ){
        HANOI(n-1, left, right, middle);
        cout << left << " => " << right << endl;
        HANOI(n-1, middle, left, right);
    }
}

int main(){
    int n;
    cin >> n;
    HANOI(n,'A','B','C');
    return 0 ;
}