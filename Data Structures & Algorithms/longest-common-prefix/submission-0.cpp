class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string sol="";
        for(int i=0;i<strs[0].size();i++){
            for(string x : strs){
                if((i==x.size()) or (x[i]!=strs[0][i])){
                    return sol;
                }
            
            }
            sol+=strs[0][i];
        }
    }
};