class Solution {
    public boolean isValid(String s) {

        int l = s.length();

        // We need even number of characters for pair matching
        if (l%2!=0) return false; 

        Stack<Character> st = new Stack<>();

        // Turn string into character array - you can do this in place inside loop too.
        char[] chars = s.toCharArray();

        for (char chr : chars) {
            // push opening chars in stack and check when a closing char comes
            if(chr == '(' || chr == '[' || chr == '{') {
                st.push(chr);
            } else if (chr == ')' || chr == ']' || chr == '}') {
                if(chr == ')') {
                    if (st.empty() || (char)st.pop()!='(') return false;
                } else if(chr == ']') {
                    if (st.empty() || (char)st.pop()!='[') return false;
                } else {
                    if (st.empty() || (char)st.pop()!='{') return false;
                }
            } else {
                return false;
            }
        }
        // stack must be empty at the end
        return st.empty();
    }
}