class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;

        for(int i = 0; i < size(nums); i++){
            if(nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
};