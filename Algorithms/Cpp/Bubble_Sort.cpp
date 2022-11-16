#include <string>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

//Developed using vectors.

void bubble_sort ( vector < pair < string , int > >& T ) {
    int n = T.size();
    for ( int i=0; i < n-1; ++i) //From i=0 to length of the vector -1
        for ( int j = n-1; j>i ; --j ) //From j = size -1 to j bigger than i 
            if ( T[j] < T[j-1]) swap ( T[j] , T[j-1]); //If position 2 smaller than position 1, swap them.
}


int main() {

    vector<pair<string, int>> seq = { {"30",1}, {"20",2} };

    bubble_sort(seq);

    for (int i = 0; i < seq.size(); ++i)
        cout << seq.at(i).first << "->" << seq.at(i).second << endl;
    return 0 ;
}
