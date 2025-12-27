class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0 , res = 0;
        HashSet<Character> store = new HashSet<>();
        for(int r = 0; r < s.length(); r++){
            while(store.contains(s.charAt(r))){
                store.remove(s.charAt(l));
                l++;
            }
            store.add(s.charAt(r));
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}