#include <string>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

/*
    Pseudocode:

    FUNCTION SUFFIX-ARRAY ():
        suffixes = dict()
        for i in |sequence|: suffixes[i] = sequence[i:]
        {print(k[0]) for k in sorted(suffixes.items(), key=lambda item: item[1])}
*/

void suffix_array(string seq) {

    vector<string> suffixes;
    map< string, int > suf; 

    //Storing data into the map.
    for ( int i=0 ; i < seq.length() ; ++i ) suf [seq.substr(i)] = i+1;

    //Output of the results.
    for (map<string,int>::iterator it=suf.begin(); it!=suf.end(); ++it)
        cout <<  it->second << endl;
}


int main(){

    string seq;
    getline(cin, seq);
    suffix_array(seq);    
    return 0;

}