#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;

bool is_palindrome(string s){
    unordered_map<char,char> D;
    int n = s.length();
    D = {{'A','T'},{'T','A'},{'C','G'},{'G','C'}};
    
    for (int i = 0; i<(n/2)+1;++i){
        if(s.at(i) != D[s.at(n-i-1)]) return false;
    }
    return true;
}

int main(){
    string s="ACCTAGGT";
    cout << (is_palindrome(s) ? "True":"False") << endl;
    return 0;
}