#include <string>
#include <iostream>

using namespace std;

int sum_of_digits(int n){
    if (n >= 0 && n<=9) return n;
    else return n%10 + sum_of_digits(n/10);
}

bool is_multiple_3(int n){
    if (sum_of_digits(n)%3 == 0) return true;
    else return false;
}


int main(){

    cout << is_multiple_3(8472) << endl;
    return 0 ;
}