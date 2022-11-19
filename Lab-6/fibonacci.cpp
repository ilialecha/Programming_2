#include <iostream>

using namespace std;

int fibonacci(int n){
    if ( n <= 1 ) return n;
    else return fibonacci(n-1) + fibonacci(n-2);
}

int main(){

    string n,m;
    while(cin >> n >> m){
        int f = fibonacci(stoi(n));
        cout << f << endl;
    }
    return 0;
}