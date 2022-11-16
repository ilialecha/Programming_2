#include <iostream>
#include <string>
#include <vector>
using namespace std;


void insertion_sort(vector< pair< int, string > >& v){

    for (int i = 1; i < v.size(); ++i){
        pair< int, string > k = v.at(i);
        int j = i - 1;
        while (j>=0 && v.at(j) > k){
            //swap(v.at(j), v.at(j-1));
            v.at(j+1) = v.at(j);
            j -= 1;
        }
        v.at(j+1) = k;
    }

}



int main() {
    
    vector<pair<int, string>> seq = { {4,"30"}, {3,"40"} };

    insertion_sort(seq);

    for (int i = 0; i<seq.size(); ++i)
        cout << seq.at(i).first << "->" << seq.at(i).second << endl;

    return 0;
}
