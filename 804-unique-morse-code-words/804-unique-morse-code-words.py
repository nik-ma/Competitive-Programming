class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        st=set()
        for i in words:
            pt=''
            for j in i:
                pt+=codes[ord(j)-ord('a')]
            st.add(pt)
        return len(st)
                