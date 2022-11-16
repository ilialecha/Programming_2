#include <string>
#include <vector>
#include <iostream>
using namespace std;

void selection_sort(vector<pair<int,string>>& v){

    for (int i = 0; i < v.size()-1; ++i){
        int small = i;
        for (int j = i + 1; j < v.size(); ++j){
            if (v.at(j).first < v.at(small).first)
                small = j;
        }
        swap(v.at(i),v.at(small));
    }

}


int main(){

    vector<pair<int, string>> seq = { {1,"30"}, {3,"40"},{6,"40"},{9,"40"},{0,"40"} };

    selection_sort(seq);

    for (int i = 0; i < seq.size(); ++i)
        cout << seq.at(i).first << "->" << seq.at(i).second << endl;

    return 0;
}