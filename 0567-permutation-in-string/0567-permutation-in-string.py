class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_freq_arr = [0] * 26
        s2_window_char_freq_arr = [0] * 26

        for i in range(len(s1)):
            s1_char_freq_arr[ord(s1[i]) - ord('a')] += 1
            s2_window_char_freq_arr[ord(s2[i]) - ord('a')] += 1
        # print(s1_char_freq_arr,s2_window_char_freq_arr)
        if s1_char_freq_arr == s2_window_char_freq_arr:
            print(s1_char_freq_arr,s2_window_char_freq_arr)
            return True

        for i in range(len(s2) - len(s1)):
            s2_window_char_freq_arr[ord(s2[i]) - ord('a')] -= 1
            s2_window_char_freq_arr[ord(s2[i + len(s1)]) - ord('a')] += 1


            if s1_char_freq_arr == s2_window_char_freq_arr:
                print(s1_char_freq_arr,s2_window_char_freq_arr)
                return True

        return False


        