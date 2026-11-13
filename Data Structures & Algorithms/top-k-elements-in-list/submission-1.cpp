class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for(int num:nums){
            m[num]++;
        }
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> h;
        for(auto& entry:m){
            h.push({entry.second,entry.first});
            if(h.size()>k){
                h.pop();
            }
        }

        vector<int> res ;
        for(int i=0;i<k;i++){
            res.push_back(h.top().second);
            h.pop();
        }
        
        return res;
    }
};
