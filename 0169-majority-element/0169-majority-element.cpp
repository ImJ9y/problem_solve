// Include the map library
#include <map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> store;
        for (int x: nums){
            store[x]++;
            if(store[x] > nums.size() / 2) return x;
        }
        return -1;
    }
};