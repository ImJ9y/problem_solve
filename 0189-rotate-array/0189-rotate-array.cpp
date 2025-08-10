class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n; // same as Python's k = k % len(nums)
        if (k == 0) return;

        // Reverse whole array
        std::reverse(nums.begin(), nums.end());

        // Reverse first k elements
        std::reverse(nums.begin(), nums.begin() + k);

        // Reverse the rest
        std::reverse(nums.begin() + k, nums.end());
    }
};