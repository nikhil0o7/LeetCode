class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> m = new HashSet<>(nums.length);
        for(int x: nums){
            if(m.contains(x)) return true;
            m.add(x);
        }
        return false;
    }
}