class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int lengthOfNum1 = size(nums1)-1;

        
        while(m > 0 && n > 0){
            if(nums1[m-1] < nums2[n-1]){
                nums1[lengthOfNum1] = nums2[n-1];
                n--;
            }
            else{
                nums1[lengthOfNum1] = nums1[m-1];
                m--;
            }
            lengthOfNum1--;
        }

        while(m > 0){
            nums1[lengthOfNum1] = nums1[m-1];
            m--;
            lengthOfNum1--;
        }

        while(n > 0){
            nums1[lengthOfNum1] = nums2[n-1];
            n--;
            lengthOfNum1--;
        }

    }
};