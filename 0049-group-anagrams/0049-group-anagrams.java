class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List> m = new HashMap<String,List>();
        for(String s: strs){
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if(!m.containsKey(key)){
                m.put(key, new ArrayList());
            }
            m.get(key).add(s);
        }
        return new ArrayList(m.values());
    }
}





