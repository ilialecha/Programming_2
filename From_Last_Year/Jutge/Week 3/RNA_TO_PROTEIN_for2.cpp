#include <iostream>
#include <map>
#include <string>

using namespace std;

string rna_prot(string seq){

    string res = "";
    int it = 0;
    int each3 = 0;

    bool start = 0;
    bool end = 0;

    //create a map that stores strings indexed by strings
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

    
    for(int i = 0; i < seq.length()-2; i++) {
        cout << seq.substr(i,3) << endl;

        if (seq.substr(i,3) == "AUG" && start == 0){
            it = i+3;
            
            start = 1;  
        
    }
    
    cout << it << endl;
    cout << start << endl;
    }
    return 0;
}
        /*
    
    while(start == 1 && end == 0){
           
        for(it; i < seq.length()-2; i++){
            //cout << it << endl;
            //cout << seq.substr(it,3) << endl;  
            if(seq.substr(it,3) == "UGA" || 
               seq.substr(it,3) == "UAA" || 
               seq.substr(it,3) == "UAG"){
                   
                   
                   end = 1;
                   break;
               }
               
            else{
                res += dic[seq.substr(it,3)];
                each3 += 3;

                if(each3%3 == 0){
                    it += 3;
                   }
               
               }
                
           }
           if(end == 0){
               break;
           }   
       }
    }
    return res;
}*/ 



int main(){

    //string seq;
    string seq = "GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA";
    //string seq = "GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGCUA";
    //cin >> seq;
    cout << rna_prot(seq) << endl;
    
}
