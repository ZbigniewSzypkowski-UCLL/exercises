def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(len(ns)):
            if ns[i] + ns[j] == target:
                return target > 0
    return False