def consecutiveLargestSubsequence(arr,l):
    val = []
    c=0
    for i in range(l):
        n=1
        while arr[i] + n in arr:
            c+=1
            n+=1
        val.append(c+1)
        c=0
    return max(val)

array = [4,6,3,5,6,7]
print("consecutive largest subsequence",consecutiveLargestSubsequence(array,len(array)))