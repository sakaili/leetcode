def longestCommonPrefix(s):
    ans = ''
    for i in zip(*s):
        if len(set(i)) ==1:
            ans+=i[0]
        else:
            break
    return ans


if __name__ == '__main__':
    s = ["flower", "flow", "flight"]
    print(longestCommonPrefix(s))
