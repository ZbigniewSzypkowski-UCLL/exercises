def median(ns):
    nls = sorted(ns)
    loc = len(nls) // 2
    if len(nls) % 2 != 0:
        return(nls[loc])
    else:
        return (nls[loc - 1] + nls[loc]) / 2