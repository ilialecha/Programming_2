#include <iostream>
#include <string>
using namespace std;

/*
Pseudocode

PROCEDURE sliding_window(sequence, x, y):
    n = len(sequence)
    for i=1 to n by step y do
        if i+x <= n do 
            SHOW sequence[i : i+x]
*/

void sliding_window(string s, int x, int y){
    for (int i = 0; i < s.length(); i+=y){
        if ( (i + x) <= s.length() )
            cout << s.substr(i,x) << endl;
    }
}

int main(){
    
    string s;
    int x;
    int y;

    cin >> s;
    cin >> x;
    cin >> y;


    sliding_window(s, x, y);

    return 0;
}