#include <vector>
#include <string>
#include <iostream>

using namespace std;

string reverse_input(string prev){
    string line;
    if (cin >> line){
        cout << reverse_input(line) << endl;
        return(prev);
    }
    else{
        return(prev);
    }
}

int main(){
    reverse_input("");
    return(0);
}