#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <stack>

using namespace std;

/*
PERMUTATIONS (s)
	let S be an empty stack (of characters)
	
	for i = 1 to |s| do
		push s[i] onto S
	
	let L be an empty set (of strings)
	insert an empty string in L
	
	while S is not empty do
		pop from S the top element x
		
		let L' be an empty set (of strings)
		
		for all w in L do
			for i = 1 to |w|+1 do
				insert w[1,...,i-1] + x + w[i,...,|w|]
				
		L = L'
		
		let A be an empty list (of strings)
		
		for all w in L do
			append w to A
		
		sort A
		
		return A
*/

vector <string> permutations(string s){

    stack<int> stack;

    for(int i = 0; i < s.length(); i++){
        stack.push(s[i]);
    }

    set <string> l = {""};
    
    while(!stack.empty()){
        
        
        char x = stack.top();
        stack.pop();
        set <string> l2;

        for(auto &w : l){
            for(int i = 0; i < w.length()+1; i++){
                l2.insert(w.substr(0,i) + x + w.substr(i));
            }
        }
        l = l2;
        
    }
    
    vector <string> A;

    for(auto &w : l){
        A.push_back(w);
    }

    sort(A.begin(), A.end());

    return A;
}

int main(){
    string s;

    cin >> s;

    for(auto &x : permutations(s)){
        cout << x << endl;
    }
}