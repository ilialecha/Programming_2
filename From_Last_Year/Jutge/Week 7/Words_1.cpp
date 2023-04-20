#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <bits/stdc++.h>
using namespace std;

/*
WORD_1(n, A)
	let L be a list with an empty string inside
	
	for i = 1 to n do
		let L' be an empty list
		
		for all w in L do
			for all x in A do
				w' = x,w
				
				append w' to L'
		
		L = L'
	
	return L
*/

vector <string> word_1(int n, vector <char> A){
    
    vector <string> l = {""};
    vector <string> l2;

    sort(A.begin(), A.end());

    for(int i = 0; i < n; i++){
        l2.clear();
        
        for (auto &w : l) {
                
            for (auto &x : A){
                string new_w = (x+w);
                l2.push_back(new_w);
                }

            }
            
        l = l2;  

        }
        
    return l;
}

int main(){
    string s;
    getline(cin, s);

    int n = stoi(s);
    getline(cin, s);

    istringstream ss(s);

    vector <char> A;
    char x;

    while(ss >> x) A.push_back(x);

    for (auto &c : word_1(n, A)){
        cout << c << endl;
    }
     
        
        
    


    

}