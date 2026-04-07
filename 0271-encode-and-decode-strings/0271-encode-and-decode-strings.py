class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + ':/' + s
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_string = []
        i = 0
        while i < len(s):
            delim = s.find(":/", i)
            len_str = int(s[i : delim])
            str_ = s[delim + 2 : delim + 2 + len_str]
            decoded_string.append(str_)
            i = delim + 2 + len_str

        return decoded_string
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))