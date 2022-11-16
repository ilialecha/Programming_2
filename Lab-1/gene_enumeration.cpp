#include <set>
#include <string>
#include <iostream>

using namespace std;

/*                                             
function gene_enumeration(s)
    n = |s|
    i = 1
    while i + 2 <= n do
        if s[i,...,i+2] = ATG then
            j = i + 3
            while j + 2 <= n do
                if s[j,...,j+2] ∈ {TAA, TAG, TGA} then
                    print s[i:j+2]
                    break
                j = j + 3
        i = i + 1
    return an empty string
*/



string gene_enumeration(string s) {

    set<string> stop = {"TAA", "TAG", "TGA"};
    int n = s.length();
    int i = 0 ;
    while (i+2 <= n) { //While i is smaller or equal than the size of the sequence.

        if (s.substr(i,3) == "ATG"){

            int j = i + 3;

            while (j + 2 <= n){

                if ( stop.find( s.substr( j, 3 ) ) != stop.end() ){
                    cout << s.substr(i, j + 2 - i + 1) << endl;
                    break;
                }
                j += 3;

            } 
        
        }

        i += 1;
    }

    return "";
}

int main() {
    string s;
    cin >> s;
    string output = gene_enumeration(s);
}