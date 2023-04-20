#include <iostream>
#include <map>
#include <string>
//GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA
using namespace std;

/*
RNA_TO_PROTEIN(S)
let protein_dict be a dictionary/map with all possible RNA codons as key and the pretein as value
	while i < |S| and not searching_start do
		if codon = "AUG" then
		searching_start <- True
		
	while i < |S| and searching_start do
		if codon = "UAA" or "UAG" or "UGA" then
			searching_end <- True
			break
			
		else res <- protein_dict[codon]
	
	if searching_start and searching_end then
		print res
*/

string rna_prot(string seq){

    string res = "";
    int i = 0;
    

    bool start = 0;
    bool end = 0;

    map<string, string> dic{
        {"AUA","I"}, {"AUC","I"}, {"AUU","I"}, {"AUG","M"},
        {"ACA","T"}, {"ACC","T"}, {"ACG","T"}, {"ACU","T"},
        {"AAC","N"}, {"AAU","N"}, {"AAA","K"}, {"AAG","K"},
        {"AGC","S"}, {"UGU","S"}, {"AGA","R"}, {"AGG","R"},                
        {"CUA","L"}, {"CTC","L"}, {"CUG","L"}, {"CUU","L"},
        {"CCA","P"}, {"CCC","P"}, {"CCG","P"}, {"CCU","P"},
        {"CAC","H"}, {"CAU","H"}, {"CAA","Q"}, {"CAG","Q"},
        {"CGA","R"}, {"CGC","R"}, {"CGG","R"}, {"CGU","R"},
        {"GUA","V"}, {"GUC","V"}, {"GUG","V"}, {"GUU","V"},
        {"GCA","A"}, {"GCC","A"}, {"GCG","A"}, {"GCU","A"},
        {"GAC","D"}, {"GAU","D"}, {"GAA","E"}, {"GAG","E"},
        {"GGA","G"}, {"GGC","G"}, {"GGG","G"}, {"GGU","G"},
        {"UCA","S"}, {"UCC","S"}, {"UCG","S"}, {"UCU","S"},
        {"UUC","F"}, {"UUU","F"}, {"UUA","L"}, {"UUG","L"},
        {"UAC","Y"}, {"UAU","Y"}, {"UAA","_"}, {"UAG","_"},
        {"UGC","C"}, {"UGU","C"}, {"UGA","_"}, {"UGG","W"}}; 

    while(i <= seq.length()-3 and start == 0 and seq != ""){

        if (seq.substr(i,3) == "AUG"){
            start = 1;
            i+=2;
        }
    i+=1;

    }
    
    while(i <= seq.length()-3 and start == 1){

        if(seq.substr(i,3) == "UGA" || 
            seq.substr(i,3) == "UAA" || 
            seq.substr(i,3) == "UAG"){
                
                end = 1;
                break;
            }
            
        else{
        
            res += dic[seq.substr(i,3)];
       }
       
       i+=3;
    }

    if (start and end){
        return res;
    }
return "";
} 


int main(){

    string seq;
    //string seq = "GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA";
    //string seq = "GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGCUA";
    cin >> seq;
    cout << rna_prot(seq) << endl;
    
}
