import numpy as np

def solve(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)

    for i in range(1, totalLength+1):
        for j in range(1, totalWeight+1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i-1, j-wlist[i]] +
                                   vlist[i], resArr[i-1, j])
            else:
                resArr[i, j] = resArr[i-1, j]
    return resArr[-1, -1], resArr


if __name__ == '__main__':
    v = [2, 3, 5, 7, 1, 4, 1]
    w = [10, 5, 15, 7, 6, 18, 3]
    weight = 15
    n = 7
    result, res = solve(v, w, weight, n)
    print("Most value:", result)
    print(res)
