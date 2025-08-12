class Solution {
public:
    int jump(vector<int>& nums) {
        int L = 0;
        int R = 0;
        int result = 0;

        while(R < size(nums)-1){
            int farthest = 0;
            for(int i = L; i <= R; i++){
                farthest = max(farthest, i + nums[i]);
            }
            L = R + 1;
            R = farthest;
            result++;
        }

        return result;
    }
};