#include <iostream>
#include <string>

using namespace std;

/*
SLIDING_WINDOW_1(S, frame, inc, i)
	return S[i...i+frame]

i <- 0	
while i <= |S|-frame do
	print SLIDING_WINDOW_1(S, frame, inc, i)
	i += inc
*/

string sliding_window(string seq, int frame, int inc, int i){

    return seq.substr(i, frame);

}

int main(){
    
    string seq;
    int frame;
    int inc;
    int i = 0;

    cin >> seq;
    cin >> frame;
    cin >> inc;

    while (i <= seq.length()-frame){
        cout << sliding_window(seq, frame, inc, i) << endl;
        i += inc;
    }


}