class Solution {
    public int search(int[] nums, int target) {
        int l = 0 , r = nums.length - 1;

        while(l < r){
            int m = (l + r) / 2;
            if(nums[m] > nums[r]){
                l = m + 1;
            } else {
                r = m;
            }
        }
        
        int pivot = l;
        r = nums.length - 1;
        l = 0;

        if(target >= nums[pivot] && target <= nums[r]){
            l = pivot;
        } else {
            r = pivot - 1;
        }

        while(l <= r) { 
            int m = (l + r)/2;
            if(target == nums[m]){
                return m;
            } else if (nums[m] < target){
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }
}