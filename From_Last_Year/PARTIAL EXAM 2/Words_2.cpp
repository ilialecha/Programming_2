#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

/*
WORDS2(n, A)
	let L be an empty list (of strings)
	insert an empty string in L
	
	sort A
	
	c = 0
	
	return WORDS2_REC(n, A, L, c)
	
WORDS2_REC(n, A, L, c)
	let L' be an empty list(of strings)
	
	for all w in l do
		for all x in A do
			w' = w,x
			
			append w' to L'
	
	L = L'
	c += 1
	
	if C != n then
		return WORD2_REC(n, A, L, c)
		
	return L
*/

vector <string> words_2(int n, vector <char> A, 
                        vector <string> l, int c);

vector <string> words_2(int n, vector <char> A){
    
    vector <string> l = {""};
    
    sort(A.begin(), A.end());
    
    int c = 0;

    return words_2(n, A, l, c);
    
}

vector <string> words_2(int n, vector <char> A, 
                        vector <string> l, int c){
                            
    vector <string> l2;

    for (auto &w : l) {
                
            for (auto &x : A){
                string new_w = (w+x);
                l2.push_back(new_w);
                }
            }
          
    l = l2;  
    c++;

    if(c != n){
            return words_2(n, A, l, c);
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

    for (auto &w : words_2(n, A)){
        cout << w << endl;
    }
}