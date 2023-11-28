public class Solution {
    public int RomanToInt(string s) {
        s = s.Replace("CM","DCCCC").Replace("CD","CCCC").Replace("XL","XXXX").Replace("XC","LXXXX").Replace("IV","IIII").Replace("IX","VIIII");
        int sum = 0;
        foreach (char i in s){
            if(i == 'M'){
                sum += 1000;
            }
            else if(i == 'D'){
                sum += 500;
            }
            else if(i == 'C'){
                sum += 100;
            }
            else if(i == 'L'){
                sum += 50;
            }
            else if(i == 'X'){
                sum += 10;
            }
            else if(i == 'V'){
                sum += 5;
            }
            else if(i == 'I'){
                sum += 1;
            }
            else{
                continue;
            }
        }

        return sum;
    }
}