class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mappings = new HashMap<>();
        mappings.put(')','(');
        mappings.put('}','{');
        mappings.put(']','[');

        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(mappings.containsKey(c)){
                if(!stack.isEmpty() && stack.peek() == mappings.get(c)){
                    stack.pop();
                } else {
                    return false;
                }
            }else{
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}