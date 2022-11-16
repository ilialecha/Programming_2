#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

int main(){

    string myString = "10 15 20 23";
    stringstream iss( myString );

    int number;
    vector<int> myNumbers;
    
    while ( iss >> number ) myNumbers.push_back( number );
    return 0;
}