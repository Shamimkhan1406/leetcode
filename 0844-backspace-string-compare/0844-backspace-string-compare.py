class Solution(object):
    def backspaceCompare(self, s, t):
        def build(string):
            st = []
            for i in string:
                if i == '#':
                    if st:
                        st.pop()
                else:
                    st.append(i)
            return ''.join(st)
        return build(s) == build(t)

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        