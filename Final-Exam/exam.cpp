#include <string>
#include <vector>
#include <set>
using namespace std;

bool palindrome(string seq){
    return true;
}

set<string> longest_palindrome_of(string sequence){
    int n = sequence.length();
    int max_len = 0;
    set<string> L = {};
    for (int i = 0; i < n-2; ++i){
        for (int j = i + 2; j < n; j=j+2){
            if (j - i >= max_len and palindrome(sequence.substr(i,j))){
                if (j - i == max_len)
                    L.insert(sequence.substr(i,j));
                else
                    L = {sequence.substr(i,j)};
            }
        }
    }
    return L;
}

int main(){
    string o = "AAAAAAAAAAAa";
    longest_palindrome_of(o);

    return 0;
}

/*
def longest_palindromes(sequence):
    n = len ( sequence )
    L = set()
    max_len = 0
    for i in range(n-2):
        for j in range(i+2,n,2):
            if j - i >= max_len:
                if palindrome(sequence[i:j]):
                    if j - i == max_len: L.add(sequence[i:j])
                    else:
                        max_len = j - i
                        L = {sequence[i:j]}
    return L
*/