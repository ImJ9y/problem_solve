class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 1;
        int count = 1;

        for(int i = 1; i < size(nums); i++){
            if(nums[i-1] == nums[i]){
                count++;
            }
            else{
                count = 1;
            }

            if(count <= 2){
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
        
    }
};