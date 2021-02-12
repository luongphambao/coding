def longestCommonPrefix(array):
        strs=array
        com = ""
        mnl = 201
        if len(strs) == 0:
            return ""
        for i in strs:
            mnl = min(mnl, len(i))
        for i in range(mnl):
            cur = strs[0][i]
            ok = True
            for j in strs[1:]:
                if cur != j[i]:
                    ok = False
            if ok: com += cur
            else: break
        return com