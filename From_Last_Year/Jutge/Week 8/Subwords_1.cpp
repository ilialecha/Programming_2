#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

/*
SUBWORDS(s)
	let S be an empty set (of strings)
	
	for i = 1 to |s| do
		for j = 1 to |s| do
			insert s[i,...,j] in S
	
	let L be an empty list (of strings)
	
	for all w in S do
		append w to L
	
	sort L
	return L
*/

vector <string> subwords(string s){

    set <string> S;

    for(int i = 0; i < s.size(); i++){
        for(int j = 0; j < s.size(); j++){
            S.insert(s.substr(i,j+1));
        }
    }

    vector <string> l;

    for (auto &w : S){
        l.push_back(w);
    }

    sort(l.begin(), l.end());

    return l;
}

int main(){
    string s;

    cin >> s;

    for(auto &x : subwords(s)){
        cout << x << endl;
    }
}