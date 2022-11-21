#include <iostream>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;
/*
def COMPLEMENTARY(s):
    D = dict()
    D['A'],D['T'] = 'T','A'
    D['C'] = 'G'
    D['G'] = 'C'
    return D[s]

def rec_palindrome(S,l):
    if 0 >= len(S)-1-l:
        return True

    if S[0] == COMPLEMENTARY(S[len(S)-1-l]):
        return rec_palindrome(S[l+1:len(S)-1-l],0)
    return False

def palindrome(S):
    if len(S) % 2 != 0: return False
    return rec_palindrome(S,0)
*/
char complementary(char c){
    unordered_map<char,char>D;
    D['A'] = 'T';D['T'] = 'A';D['C'] = 'G';D['G'] = 'C';
    cout << D[c] << endl;

    return D[c];
}


bool rec_palindrome(string S, int l){
    if (0 >=S.size()-1-l) return true;
    if (S.at(0) == complementary( S.at(S.size()-1-l)) ){
        cout << S.size()-1-l << endl;
        return rec_palindrome( S.substr(l+1,-2) ,0);
        }
    else return false;
}

bool palindrome(string S){
    if (S.length() % 2 != 0) return false;
    else return rec_palindrome(S,0);
}


int main(){
    string S = "TTTAAA";
    bool p = palindrome(S);
    cout << p << endl;
}