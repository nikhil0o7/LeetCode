class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n

        fid, typ, time = logs[0].split(":")
        stack.append(int(fid))
        prev = int(time)
        i = 1
        while i < len(logs):
            fid, typ, time = logs[i].split(":")
            t = int(time)

            if typ == "start":
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(int(fid))
                prev = t
                
            elif typ == "end":
                res[stack[-1]] += t - prev + 1
                stack.pop()
                prev = t + 1

            i +=1 

        return res 
        