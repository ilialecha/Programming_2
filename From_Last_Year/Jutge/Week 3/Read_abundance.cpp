#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

/*
READ_ABUNDANCE(S)
	if S not in dict and comp_rev(S) not in dict then
		dict[minimum of S and comp_rev(S)] = 1
	
	else dict[minimum of S and comp_rev(S)] += 1
*/

string comp_rev(string seq){

  string res;

  map<char, char> dic{
        {'A','T'}, {'T','A'}, {'C','G'}, {'G','C'}}; 
  
  for(int i = 0; i < seq.length(); i++){
    res += dic[seq[i]];
  }
  
  reverse(res.begin(), res.end());
  return res;
}


int main(){

  map<string, int> d2;

  string seq;

  while(cin >> seq){
    
    if(d2.count(seq) == 0 && d2.count(comp_rev(seq)) == 0){
      d2.insert(pair<string, int>((min(seq, comp_rev(seq))), 1));
  }
  
  else{
    d2[(min(seq, comp_rev(seq)))]++;
    }
  }

for (const auto &x : d2)
    cout << x.first << " " << x.second << endl;


  
}


