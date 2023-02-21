from math import floor


def jaroDis(s1, s2):
    if (s1 == s2):
        return 1.0
    len1 = len(s1)
    len2 = len(s2)

    # Identify maximum distance between the strings
    max = floor(max(len1, len2) / 2 ) - 1
    match = 0
    hash1 = [0] * len(s1)
    hash2 = [0] * len(s2)

    for i in range(len1):
        for j in range(max(0, i - max), min(len2, i + max +1)):
            hash1[i] = 1
            hash2[j] = 1
            match += 1
            break
    if (match == 0):
        return 0.0
    trans = 0
    point = 0

    for i in range(len1):
        if (hash1[i]):
            while (hash2[point] == 0):
                point += 1
            if (s1[i] != s2[point]):
                trans += 1
            point +=1
    trans = trans//2
    return (match/ len1 + match / len2 + (match - trans) /match)/ 3.0

print(jaroDis("fuck", "FUCK"))