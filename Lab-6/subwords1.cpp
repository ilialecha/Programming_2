/*
    FUNCTION SUBWORDS(S):
        #Set for avoiding repeated subwords.
        Let W be an empty set(of strings)
        for i = 1 up to |S| do
            for j = i up to |S| do
                insert S[i:j] into W
        Let L be an empty list(of strings)
        for all w € W do:
            append w into L
        sort L
        return L
*/
#include <string>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> subwords( string& S ){
    set<string> W;
    for ( int i = 0; i < S.length(); ++i )
        for ( int j=i; j < S.length(); ++j )
            W.insert( S.substr( i, j - i + 1 ) );
    
    vector<string> L;
    
    for ( auto w : W ) L.push_back( w );

    sort( L.begin(), L.end() );
    
    return L;
    
}

int main(){

    string S;

    getline(cin,S);

    vector<string> L = subwords(S);

    for ( auto l : L ) cout << l << endl;

    return 0 ; 
}