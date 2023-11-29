public class Solution {
    public int HammingWeight(uint n) {
        int result = (int) n;
        string binary = Convert.ToString(result, 2);
        int sum = 0;
        
        for(int i = 0; i < binary.Length; i++){
            if(binary[i] == '1'){
                sum += 1;
            }
        }
        
        return sum;
    }
}