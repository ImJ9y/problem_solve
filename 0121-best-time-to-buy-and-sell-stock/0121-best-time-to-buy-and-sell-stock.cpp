class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curr = prices[0];
        int total = 0;

        for(int price: prices){
            if(curr < price){
                total = max(total, price-curr);
            }
            else{
                curr = price;
            }
        }

        return total;
    }
};