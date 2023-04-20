#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

/*
SUBWORDS(s)
	S1, S2 = SUBWORDS_REC(s, 0)
	
	let L be an empty list (of strings)
	
	for all w in S2 do 
		append w to L
	
	sort L
	return L
	
SUBWORDS_REC(s, i)
	if i > |s| then
		return {}, {}
	
	else
		S1, S2 = SUBWORDS_REC(s, i+1)
		
		insert the empty string in S1
		
		for all w in S1 do
			for j = 1 to |s| do
				insert s[i,.......,j+1] in S2
	
	return S1, S2	
*/

set <string> subwords2(string s, int i);

vector <string> subwords2(string s){
    
    set <string> S1 = subwords2(s,0);
    set <string> S2 = subwords2(s,0);
    
    vector <string> l; 

    for(auto &w : S2){
        l.push_back(w);
    }

    sort(l.begin(), l.end());

    return l;

}


set <string> subwords2(string s, int i){

    set <string> S1;
    set <string> S2;

    if (i > s.length()){
        
        set <string> S1;
        set <string> S2;
        return S1, S2;
    }

    else{
        
      set <string> S1 = subwords2(s, i+1);
      set <string> S2 = subwords2(s, i+1);
    }

    S1.insert("");

    for(auto &w : S1){
        
        for(int j = 0; j < s.size(); j++){
            S2.insert(s.substr(i,j+1));
            S2.insert(s.substr(3,j+1));
            S2.insert(s.substr(2,j+1));
            

            if(i < s.length()){
                
                S2.insert(s.substr(i+1,j+1));
                
            }
            
            
            
        }
    }

    return S1, S2;
}

int main(){
    string s;

    cin >> s;
    
    for(auto &x : subwords2(s)){
        cout << x << endl;
    }
}