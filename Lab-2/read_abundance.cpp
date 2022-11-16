#include <map>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

/*
function reverse-complement(s):
    let C be an empty dictionary
    C = { 'A' : 'T' , 'C' : 'G' , 'G' : 'C' , 'T' : 'A'}
    for i=1 to |s| do
        s[i] = C[ s[n-(i-1)] ]
    return s 

function read_abundance(seq):
    let d be a dictionary
    for character in char_sequence do 
        r = reverse_complement(character)
        if r < s:
            s = r
        d[s] = 1 if empty or d[s]+1 if not empty
    return d 
    
*/

string reverse_complement ( string s );

map < string , int > read_abundance ( const vector < string >& S );

string reverse_complement ( string s ) {

    string t ( s );
    map < char , char > C = {{'A' ,'T'} , { 'C' , 'G'} , { 'G' , 'C'} , { 'T' , 'A' }};

    for ( int i = 0; i < int ( s . length ()); i++ )
        t [ i ] = C [ s [ s . length () - ( i + 1)]];
        
    return t;
}

map < string , int > read_abundance ( const vector < string >& S ) {
    map < string , int > D ;
    for ( auto s : S ) {
        if ( D . find ( s) != D . end ()) {
            D [ s ] += 1;
        }  
        else D [ s ] = 1;
    }
    return D ;
}


int main(){

    vector <string> S;
    string s;
    while (cin >> s) {
        string t = reverse_complement(s);
        if ( t < s ) s = t ;
        S.push_back(s);
    }

    map < string , int > D = read_abundance ( S );
    for ( auto item : D ) {
        cout << item . first << " " << item . second << endl ;
    }
    
}