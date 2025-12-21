class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        for(int x: nums){
            if(m.containsKey(x)) return true;
            m.put(x, x);
        }
        return false;
    }
}