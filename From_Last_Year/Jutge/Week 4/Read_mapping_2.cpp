#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

/*
BUBBLE_SORT(A)
let A be an array with each value being each suffix with its position
	for i = 1 to |A| - 1 do 
		for j = |A| downto i + 1 --- 
			if A[j] < A[j+1] then 
				exchange A[j] with A[j+1] 
*/
using namespace std;

int main(){

    string seq;
    cin >> seq;
    
    vector< pair <string, int> > l;
    if(seq != ""){

        for(int i = 0; i < seq.length(); i++){
        l.push_back(make_pair(seq.substr(i,seq.length()), i+1));
    }

    int n = size(l);
    
    for(int i = 0; i < n; i++){
        for(int j = n-1; j >= 0; j--){
            if (l[j].first < l[j+1].first){
                swap(l[j], l[j+1]);
            }
        }
    }
   
    reverse(l.begin(),l.end());

    for(const auto &x : l){
        cout << x.second << endl;
    }
    }
    
    
    

}
