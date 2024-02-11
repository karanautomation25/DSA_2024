# Longest Substring With Without Repeating Characters

def LongestSubstrKUnique(strng, n, k):
    hashmap = dict()
    start = 0
    end = 0
    max_substr_len = 0

    while end < n:
        curr_ch = strng[end]
        if curr_ch in hashmap:
            hashmap[curr_ch] += 1

        else:
            hashmap[curr_ch] = 1

        # update the end pointer
        end += 1

        while len(hashmap) < end - start + 1:
            ch_front = strng[start]

            hashmap[ch_front] -= 1

            # check that the count of curr_ch is 0 or not
            if hashmap[ch_front] == 0:
                del hashmap[ch_front]

            start += 1

        # Update the max_substr_len with k or less then k unique characters
        max_substr_len = max(max_substr_len, end - start)

    return max_substr_len