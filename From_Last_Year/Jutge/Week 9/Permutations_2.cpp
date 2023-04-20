#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <stack>

using namespace std;

/*
PERMUTATIONS (s)
	L = PERMUTATIONS ("", s)
	
	let A be an empty list (of strings)
	
	for all w in L do
		append w to A
	
	sort A
	return A
	
	
PERMUTATIONS(prefix, s)
	let L be an empty set (of strings)
	
	if |s| = 0 then
		insert prefix in L
	
	else
		for i = 1 to |s| do 
			for all w in PERMUTATIONS(prefix + s[i], s[1,...,i-1] + s[i+1,...,|s|]) do
				insert w in L
	
	return L
*/

set <string> permutations(string prefix, string s);

vector <string> permutations(string s){

    vector <string> A;

    for(auto &w : permutations("", s)){
        A.push_back(w);
    }

    sort(A.begin(), A.end());

    return A;

}

set <string> permutations(string prefix, string s){

    set <string> L;

    if(s.length() == 0){
        L.insert(prefix);
    }

    else{
        for(int i = 0; i < s.length(); i++){
            for(auto &w : permutations(prefix + s[i], 
                                s.substr(0,i) + s.substr(i+1))){
                                    L.insert(w);
                                }
        }
    }

    return L;
}

int main(){

    string s;

    cin >> s;

    for(auto &x : permutations(s)){
        cout << x << endl;
    }
}