#include <iostream>
#include <string>
/*
def gene_find(seq):
	.
	.
	.

i <- 0

while i < |seq| do
	if seq[i:i+3] == "ATG" THEN
		if gene_find(seq[i:|seq|]) is not nil then
			return gene_find(seq[i:|seq|])
	
	i+=1
*/

using namespace std;
string seq;
string res = "";

string gene_find(string seq){

    
    bool searching_start = 1;
    bool found_end = 0;
    res = "";
    int i = 0;
    
    while (searching_start == 1 and i < seq.length()-3){
        
        if (seq.substr(i,3) == "ATG"){
            res+=seq.substr(i,3);
            searching_start = 0;
            i+=3;
            break;
        }
    i++;
    }

    while (searching_start == 0 and i < seq.length()-3){
         
        res+=seq.substr(i,3);
        
        if(seq.substr(i,3) == "TAA" || seq.substr(i,3) == "TAG" 
        || seq.substr(i,3) == "TGA"){
            found_end = 1;
            break;
        }
        
        i+=3;
    }

   if (found_end == 1){
       return res;
   }
   else{
       return "None";
   }
   
}

int main(){
    int i = 0;

    string seq;
    cin >> seq;

    while(i < seq.length()){
        //cout << endl;
        //cout << seq.substr(i,seq.length()) << endl;
        //cout << seq.substr(i,3) << endl;
        if (seq.substr(i,3) == "ATG"){
            if (gene_find(seq.substr(i,seq.length())) != "None"){
                
                
                cout << gene_find(seq.substr(i,seq.length())) << endl;

            }
        }
        res = "";
        i++;
    }
 
    }
//input: GAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAGTCGAAAAATTATCTTGATAAAGCAGGAATTACTACTGCTTGTTTACGAATTAAATCGAAGTGGACTGCTGGCGGAAAATGAGAAAATTCGACCTATCCTTGCGCAGCTCGAGAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGTCAAGGACTGGTTTAGATATGAGTCACATTTTGTTCATGGTAGAGATTCTCTTGTTGACATTTTAAAAGAGCGTGGATTACTATCTGAGTCCGATGCTGTTCAACCACTAATAGGTAAGAAATCATGAGTCAAGT