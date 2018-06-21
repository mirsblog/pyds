def twoSum(data, target):

    # brute force
    # O(n^2)
    # no extra space
    for (index1, value1) in enumerate(data):
        diff = target-value1
        for (index2, value2) in enumerate(data):
            # can't use same index
            if index2 == index1:
                continue
            if value2 == diff:
                return (index1, index2)

def twoSum1(data, target):

    # using hashmap
    # O(n)
    # O(n) space too
    m = {}
    for (index1, value1) in enumerate(data):
        diff = target - value1
        if diff in m:
            return (index1, m[diff])
        m[value1] = index1

if __name__ == "__main__":
    data = [0, -2,7,0, 11,15]
    print(twoSum(data, 0))
    print(twoSum1(data, 0))
