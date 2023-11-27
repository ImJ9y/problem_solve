public class Solution {
    public bool IsPalindrome(int x) {
        string toStrNum = x.ToString();
        string convNum = "";
        for(int i = toStrNum.Length-1; i >= 0; i--){
            convNum += toStrNum[i];
        }
        return(toStrNum == convNum);
    }
}