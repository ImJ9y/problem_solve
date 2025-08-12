class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = size(nums)-1;

        for(int i = size(nums)-1; i >= 0; i--){
            int length = i + nums[i];

            if(length >= goal){
                goal = i;
            }
        }
        return goal == 0;
    }
};