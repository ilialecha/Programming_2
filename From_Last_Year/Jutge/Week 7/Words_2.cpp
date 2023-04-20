#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <bits/stdc++.h>
using namespace std;

/*
WORD2(n, A)
	let L be an empty list
	insert an empty string to L
	
	sort A
	
	C = 0
	
	return WORD2_REC(n, A, L, C)
	
WORD2_REC(n, A, L, C)
	let L' be an empty list
	
	for all w in l do
		for all x in A do
			w' = w,x
			
			append w' to L'
	L = L'
	C += 1
	
	if C != n then
		return WORD2_REC(n, A, L, C)
		
	return L
*/

vector <string> word_2(int n, vector <char> A, 
                        vector <string> l, int count);

vector <string> word_2(int n, vector <char> A){
    
    vector <string> l = {""};
    
    sort(A.begin(), A.end());
    
    int count = 0;

    return word_2(n, A, l, count);
    
}

vector <string> word_2(int n, vector <char> A, 
                        vector <string> l, int count){
                            
    vector <string> l2;

    for (auto &w : l) {
                
            for (auto &x : A){
                string new_w = (x+w);
                l2.push_back(new_w);
                }
            }
          
    l = l2;  
    count++;

    if(count != n){
            return word_2(n, A, l, count);
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

    for (auto &c : word_2(n, A)){
        cout << c << endl;
    }
}