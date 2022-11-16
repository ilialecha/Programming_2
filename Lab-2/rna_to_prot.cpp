#include <set>
#include <string>
#include <iostream>
#include <map>
#include <unordered_map>
using namespace std;


string gene_finding(string s) {

    set<string> stop = {"UAA", "UAG", "UGA"};
    int n = s.length();
    int i = 0 ;
    while (i+2 <= n) { //While i is smaller or equal than the size of the sequence.

        if (s.substr(i,3) == "AUG"){

            int j = i + 3;

            while (j + 2 <= n){

                if ( stop.find( s.substr( j, 3 ) ) != stop.end() ){
                    return s.substr(i, j + 2 - i + 1);
                }
                j += 3;

            } 
        
        }

        i += 1;
    }

    return "";
}

string rna_translated(string frame){

    unordered_map <string, string> codon_map;

    codon_map["UUU"] = "F";
    codon_map["UUC"] = "F";
    codon_map["UUA"] = "L";
    codon_map["UUG"] = "L";
    codon_map["UCU"] = "S";
    codon_map["UCC"] = "S";
    codon_map["UCA"] = "S";
    codon_map["UCG"] = "S";
    codon_map["UAU"] = "Y";
    codon_map["UAC"] = "Y";
    codon_map["UAA"] = "*";
    codon_map["UAG"] = "*";
    codon_map["UGU"] = "C";
    codon_map["UGC"] = "C";
    codon_map["UGA"] = "*";
    codon_map["UGG"] = "W";
    codon_map["CUU"] = "L";
    codon_map["CUC"] = "L";
    codon_map["CUA"] = "L";
    codon_map["CUG"] = "L";
    codon_map["CCU"] = "P";
    codon_map["CCC"] = "P";
    codon_map["CCA"] = "P";
    codon_map["CCG"] = "P";
    codon_map["CAU"] = "H";
    codon_map["CAC"] = "H";
    codon_map["CAA"] = "Q";
    codon_map["CAG"] = "Q";
    codon_map["CGU"] = "R";
    codon_map["CGC"] = "R";
    codon_map["CGA"] = "R";
    codon_map["CGG"] = "R";
    codon_map["AUU"] = "I";
    codon_map["AUC"] = "I";
    codon_map["AUA"] = "I";
    codon_map["AUG"] = "M";
    codon_map["ACU"] = "T";
    codon_map["ACC"] = "T";
    codon_map["ACA"] = "T";
    codon_map["ACG"] = "T";
    codon_map["AAU"] = "N";
    codon_map["AAC"] = "N";
    codon_map["AAA"] = "K";
    codon_map["AAG"] = "K";
    codon_map["AGU"] = "S";
    codon_map["AGC"] = "S";
    codon_map["AGA"] = "R";
    codon_map["AGG"] = "R";
    codon_map["GUU"] = "V";
    codon_map["GUC"] = "V";
    codon_map["GUA"] = "V";
    codon_map["GUG"] = "V";
    codon_map["GCU"] = "A";
    codon_map["GCC"] = "A";
    codon_map["GCA"] = "A";
    codon_map["GCG"] = "A";
    codon_map["GAU"] = "D";
    codon_map["GAC"] = "D";
    codon_map["GAA"] = "E";
    codon_map["GAG"] = "E";
    codon_map["GGU"] = "G";
    codon_map["GGC"] = "G";
    codon_map["GGA"] = "G";
    codon_map["GGG"] = "G";


    string prot = "";
    
    if (frame.length()% 3 == 0) {
        int i = 0;

        for (int i = 3; i < frame.length()-3;i+=3){
            //cout << frame.substr(i,3) << "\n";

            if (codon_map.find(frame.substr(i,3)) != codon_map.end()){
                prot += codon_map[frame.substr(i,3)] ;
            }

        }
        return prot;
    }
    return "";
}


int main(){

    string s;
    cin >> s;
    string output = gene_finding(s);

   if (output.length() > 0){
        //Here run function translation.
        string translation = rna_translated(output);
        if (translation.length()>0){
            cout << translation << endl;
        }
    }
        
}