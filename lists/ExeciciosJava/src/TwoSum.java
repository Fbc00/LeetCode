import java.util.Arrays;

public class TwoSum {
    int[] vect = new int[2];
    public int[] twoSum(int[] nums, int target) {
        int aux;
        for(int i=0; i<nums.length; i++){
            aux = i;
            for(int x=aux+1; x<nums.length; x++){
                if(nums[i] + nums[x] == target) {
                    vect[0] = i;
                    vect[1] = x;
                }
            }
            aux = 0;
        }
        return vect;
    }

}
