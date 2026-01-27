class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;


        for(int i = 0; i < flowerbed.length; i++){
            boolean left = i == 0 || flowerbed[i-1] == 0 ? true:false;
            boolean right = i == flowerbed.length-1 || flowerbed[i+1] == 0 ? true:false;

            if(flowerbed[i]==0 && left && right){
                flowerbed[i] = 1;
                count++;
            }
        }

        return count >= n;
    }
}