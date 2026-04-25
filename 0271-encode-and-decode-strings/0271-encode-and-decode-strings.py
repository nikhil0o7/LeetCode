class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            curr_s =  str(len(s)) +  ':/' + s
            print(curr_s)
            encoded_str += curr_s
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []
        i = 0
        while i < len(s):
            delim = s.find(':/',i)
            length = int(s[i:delim])
            curr_s = s[delim+2 : delim+2+length]
            decoded_str.append(curr_s)
            i = length +delim + 2

        return decoded_str
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))