def compare_version_numbers(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    max_len = max(len(v1), len(v2))
    v1 = v1 + [0] * (max_len - len(v1))
    v2 = v2 + [0] * (max_len - len(v2))
    for i in range(max_len):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1
    return 0
    def compare_version_numbers(version1, version2):
     v1 = version1.split('.')
    v2 = version2.split('.')
    max_len = max(len(v1), len(v2))
    v1 = v1 + [0] * (max_len - len(v1))
    v2 = v2 + [0] * (max_len - len(v2))
    for i in range(max_len):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1
    return 0