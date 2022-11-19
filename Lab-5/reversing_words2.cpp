#include <vector>
#include <string>
#include <iostream>

using namespace std;

string reverse_input(string prev){
    string line;
    cin >> line;
    if (line == "end"){
        return prev;
    }
    else{
        cout << reverse_input(line) << endl;
        return(prev);
    }
}

int main(){
    reverse_input("");
    return(0);
}