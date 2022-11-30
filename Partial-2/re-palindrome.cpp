#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

bool rec_palindrome(const string &S, int low, int high, const unordered_map<char, char> &D){
    if (low>=high)
        return true;
    if ( S.at(low) == D.at(S.at(high)) ) 
        return rec_palindrome(S, low+1, high-1, D);
    return false;
}

bool palindrome( const string &S){
    int n = S.size();
    if (n % 2 != 0)
        return false;
    if (n == 0)
        return true;
    unordered_map<char, char> D = {{'A','T'}, {'A','T'}, {'A','T'}, {'A','T'}};
    return rec_palindrome(S,0,n-1,D);
}

int main(){
    string S = "AAATTT";

    cout << (palindrome(S) ? "True":"False") << endl;

}