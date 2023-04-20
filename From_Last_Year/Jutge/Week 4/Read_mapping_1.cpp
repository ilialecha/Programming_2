#include <iostream>
#include <string>
#include <map>
/*
READ_MAPPING1(S)
	let de b empty dictionary
	for i = 0 to |S| do
		d[S[i:]] <-  i+1
		for x in sorted(d) do
			print(d[x])
*/
using namespace std;

int main(){

    map <string, int> d;

    string seq;

    cin >> seq;

    for(int i = 0; i < seq.length(); i++){
        d[seq.substr(i,seq.length())] = i+1;
    }

    for (const auto &x : d){
        cout << x.second << endl;
    }
    
}