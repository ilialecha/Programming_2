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

void bubble_sort ( vector < pair < int , string > >& T ) {
    int n = T.size();
    for ( int i=0; i < n-1; ++i) //From i=0 to length of the vector -1
        for ( int j = n-1; j>i ; --j ) //From j = size -1 to j bigger than i 
            if ( T[j].second < T[j-1].second) swap ( T[j] , T[j-1]); //If position 2 smaller than position 1, swap them.
}

void printVector(vector<pair<int,string>>& v){
    for (int i = 0; i < v.size(); ++i) cout << v.at(i).first << endl;
}

void suffix_array(string seq) {

    vector< pair< int, string > > suff;

    //Storing data into the map.
    for ( int i=0 ; i < seq.length() ; ++i ) suff.push_back(make_pair( i+1, seq.substr(i) ));
    //Sorting the data.
    bubble_sort(suff);

    printVector(suff);


}


int main(){

    string seq;
    getline(cin, seq);
    suffix_array(seq);
    return 0;

}