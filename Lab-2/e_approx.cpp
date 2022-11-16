#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int factorial(int i){
    if (i==0) return 1;
    else return i * factorial(i-1);
}

double e_approximation(int i){
    if (i==0) 
    return 0;
    else 
    return (double) i/factorial(i) + e_approximation(i-1);
}


int main(){

    int i = 20;
    cout <<setprecision(11) << e_approximation(i) <<endl;

}