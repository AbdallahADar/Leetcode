def lengthOfLongestSubstring_bruteforce(s):
    """
    :type s: str
    :rtype: int
    """
    
    ret=0
    index=0
    
    for i in s:
        index+=1
        M=[i]
        for j in s[index:]:
            if j in M:
                break
            else:
                M.append(j)
        ret=max(len(M),ret)
        
    return ret
    
    
def lengthOfLongestSubstring_dynamic_lists(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0

    cur_l = [s[0]]
    max_l = 1

    for i in range(1,len(s)):

        if s[i] not in cur_l:
            cur_l.append(s[i])
        else:
            cur_l = cur_l[cur_l.index(s[i])+1:]
            cur_l.append(s[i])

        if len(cur_l) > max_l:
            max_l = len(cur_l)

    return max_l
    
    
    
def lengthOfLongestSubstring_dynamic_indexing(s):
    """
    :type s: str
    :rtype: int
    """
    
    if len(s) == 0:
            return 0

    l = 0
    max_l = 1

    for i in range(1,len(s)):

        if s[i] in s[l:i]:
            l = s[l:].index(s[i])+l+1

        if i-l+1 > max_l:
            max_l = i-l+1

    return max_l