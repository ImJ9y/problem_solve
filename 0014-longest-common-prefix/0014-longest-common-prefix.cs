public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
        
        string result = "";
        
        if(strs == null || strs.Length == 0){
            return result;
        }

        string checkedWord = strs[0];
        for (int i=1; i<strs.Length; i++)
        {
            while(strs[i].IndexOf(checkedWord) != 0) // IndexOf == find in python
            {
                checkedWord = checkedWord.Substring(0,checkedWord.Length-1);
            }
        }
        return checkedWord;
    }
}