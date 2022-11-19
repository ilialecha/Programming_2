#include <vector>
#include <string>
#include <iostream>
using namespace std;

string reverse_input( signed int n, string prev ){
    string new_input = "";
    cin >> new_input;

    if (n == 0) return( prev );
    else{
        if ( n < 0 ){
            reverse_input( stoi(new_input) , "");
            return( prev );
        }
        else{
            cout << reverse_input( n - 1 , new_input ) << endl;
            return( prev );
        }
    }
}

int main(){
    reverse_input( -1 , "");
    return(0);
}