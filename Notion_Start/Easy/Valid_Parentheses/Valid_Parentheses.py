class Solution:
    def isValid(self, s: str) -> bool:
        
        l = len(s)
        # We need even number of characters for pair matching
        if l%2:
            return False
        
        # initialize the stack
        st = []

        for c in s:
            # push opening chars in stack and check when a closing char comes
            if c=='(' or c=='{' or c=='[':
                st.append(c)
            elif c==')' or c=='}' or c==']':
                if c==')':
                    if len(st)==0 or st.pop()!='(':
                        return False
                elif c==']':
                    if len(st)==0 or st.pop()!='[':
                        return False
                else:
                    if len(st)==0 or st.pop()!='{':
                        return False
            else:
                return False
        # stack must be empty at the end\
        return len(st)==0