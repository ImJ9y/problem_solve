public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for(int i = 0; i < nums.Length; i++){
            for(int j = 1; j < nums.Length; j++){
                if(i==j){
                    continue;
                }
                if(nums[i] + nums[j] == target){
                    return new int[] { i, j };
                }
            }
        }
        throw new ArgumentException("No solution found");
    }
}