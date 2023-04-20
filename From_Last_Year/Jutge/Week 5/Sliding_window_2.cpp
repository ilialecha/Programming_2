#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
let L be an empty vector

SLIDING_WINDOW(S, frame, inc)
	return SLIDING_WINDOW_REC(S, frame, inc, 0)

SLIDING_WINDOW_REC(S, frame, inc, i)
	append seq[i:i+frame] to L
	
	while i <= |S|-frame then
		return SLIDING_WINDOW_REC(S, frame, inc, i+inc)
	
	return l

*/


vector <string> A;

vector <string> sw(string seq, int frame, int inc, int i);

vector <string> sw(string seq, int frame, int inc){
    return sw(seq, frame, inc, 0);
      
}

vector <string> sw(string seq, int frame, int inc, int i){
    
    if(i <= seq.length()-frame){
        A.push_back(seq.substr(i, frame));
        sw(seq, frame, inc, i+inc);
    }
    return A;
}    

int main()
{
    string seq;
    int frame;
    int inc;

    cin >> seq;
    cin >> frame;
    cin >> inc;

   for(auto &x : sw(seq, frame, inc)){
       cout << x << endl;
   }
   
    
}
