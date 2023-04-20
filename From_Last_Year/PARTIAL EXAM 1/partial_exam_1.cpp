#include <iostream>
#include <string>
#include <map>
/*
WORD_COMPOSITION(S, n)
	let d be an empty dictionary
	
	for i = 0 to |S| do
		
		substring <- seq[i...i+n]
		
		if substring not in d then
			if |substring| == n then
				d[substring] <- 1
		else 
			d[substring] += 1
		
	return d
*/

using namespace std;

map <string, int> word_composition(string seq, int n){
    
    map <string, int> d;

    for(int i = 0; i < seq.length(); i++){
        
        string substr = seq.substr(i, n);

        if (d.count(substr) == 0){
            if (substr.length() == n){
                d.insert(pair<string, int>(substr, 1));
            }
        }

        else {
            d[substr] ++;

        }
 
    }
    return d;
}

/*
d.find(substr) != d.end() = ENCONTRADO/ESTA DENTRO
d.find(substr) == d.end() = NO ENCONTRADO/NO ESTA DENTRO
*/



int main(){

    string seq;
    int n ;

    cin >> seq;
    cin >> n;

    for (auto &x : word_composition(seq, n)){
        cout << x.first << " " << x.second << endl;
    }
}