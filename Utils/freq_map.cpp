#include <map>
#include <string>
#include <vector>

using namespace std;

map <string , int >freq_distribution(const vector<string>& S) {
    map <string , int > D;
    for (auto s : S) {
        if (D.find(s) == D.end())D[s] = 1;
        else D[s] += 1;
    }
    for (auto it = D.begin(); it != D.end(); ++it){
        cout << it->first << " " << it->second << endl;
    }

    return D;
}
